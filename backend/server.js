require('dotenv').config();
const sendDiscordAlert = require("./discordAlertApiFail.js");

console.log("NODE_ENV =", process.env.NODE_ENV);

// NEW
if (process.env.NODE_ENV === "test") {
  console.log("Running in test mode: axios is mocked");
  require('./axiosMock.js');

  // Mock native fetch for LiteLLM calls
  global.fetch = async (url, options) => {
    if (url.includes('litellm')) {
      return {
        ok: true,
        json: async () => ({
          choices: [{
            finish_reason: 'stop',
            message: {
              content: 'This is a mocked response from LiteLLM ✅',
              tool_calls: null
            }
          }]
        })
      };
    }
    // fallback to real fetch for other URLs
    return globalThis.fetch(url, options);
  };
}

const express = require('express');
const axios = require('axios');
const cors = require('cors');
const redisClient = require('./redis'); // Import Redis client
const { Client } = require('@modelcontextprotocol/sdk/client/index.js');
const { SSEClientTransport } = require('@modelcontextprotocol/sdk/client/sse.js');


const app = express();
const port = 5000;

const corsOptions = {
  origin: ['https://www.limjiajing.com',],  // Frontend domain
  methods: ['GET', 'POST', 'OPTIONS'],
  allowedHeaders: ['Content-Type', 'Authorization'],
  credentials: true,  // Allow credentials (cookies) to be sent
};

app.use(cors(corsOptions));  // Apply CORS options
app.use(express.json());

// Debugging logs
console.log("Server starting...");
console.log("NODE_ENV:", process.env.NODE_ENV || "not set");
console.log("GEMINI API Key:", process.env.GEMINI_API_KEY ? "Loaded" : "Not Found");
console.log("OpenRouter API Key (fallback):", process.env.OPENROUTER_API_KEY ? "Loaded" : "Not Found");

// ── LiteLLM helper using native fetch (Node v18+) ────────────────────────────
async function litellmChat(body) {
  const response = await fetch('http://litellm:4000/chat/completions', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      'Authorization': 'Bearer dummy'
    },
    body: JSON.stringify(body)
  });
  if (!response.ok) {
    const err = await response.text();
    throw new Error(`LiteLLM ${response.status}: ${err}`);
  }
  return response.json();
}

// ── MCP Client helpers ───────────────────────────────────────────────────────

async function getMCPTools() {
  const transport = new SSEClientTransport(
    new URL('http://mcp-server:8000/sse')
  );
  const client = new Client({ name: 'portfolio-backend', version: '1.0.0' });
  await client.connect(transport);
  const { tools } = await client.listTools();
  await client.close();

  // Convert MCP tool format to OpenAI function calling format
  return tools.map(tool => ({
    type: 'function',
    function: {
      name: tool.name,
      description: tool.description,
      parameters: tool.inputSchema
        ? JSON.parse(JSON.stringify(tool.inputSchema))  // deep clone to remove circular refs
        : { type: 'object', properties: {} }
    }
  }));
}

async function callMCPTool(toolName, args) {
  const transport = new SSEClientTransport(
    new URL('http://mcp-server:8000/sse')
  );
  const client = new Client({ name: 'portfolio-backend', version: '1.0.0' });
  await client.connect(transport);
  const result = await client.callTool({ name: toolName, arguments: args });
  await client.close();
  return result.content[0].text;
}

app.post('/api/chat', async (req, res) => {
  const { message } = req.body;

  if (!message) {
    return res.status(400).json({ error: 'Message is required' });
  }

  try {
    // Check Redis cache
    const cachedResponse = await redisClient.get(message);
    if (cachedResponse) {
      console.log('Returning cached response');
      return res.json({ botResponse: cachedResponse });
    }

    // Get tools from MCP server
    const tools = await getMCPTools();
    console.log(`Loaded ${tools.length} MCP tools`);

    const messages = [
      {
        role: 'system',
        content: `You are an AI assistant for Jia Jing's portfolio website.
Use the available tools to fetch information, then summarize the results in a friendly, concise way.
Never return raw tool calls or code blocks in your response.
Always provide a human-readable answer based on the tool results.`
      },
      { role: 'user', content: message }
    ];

    // First LLM call — with tools
    const firstData = await litellmChat({ model: 'portfolio-default', messages, tools });
    const firstChoice = firstData.choices[0];

    // If LLM wants to call a tool
    if (firstChoice.finish_reason === 'tool_calls' && firstChoice.message.tool_calls) {
      const toolCall = firstChoice.message.tool_calls[0];
      const toolName = toolCall.function.name;
      const toolArgs = JSON.parse(toolCall.function.arguments || '{}');

      console.log(`MCP tool called: ${toolName}`, toolArgs);

      // Call the tool via MCP server
      const toolResult = await callMCPTool(toolName, toolArgs);
      console.log(`Tool result type: ${typeof toolResult}`);
      console.log(`Tool result preview: ${String(toolResult).substring(0, 100)}`);
      console.log(`MCP tool result received for: ${toolName}`);

      // Second LLM call — with tool result
      messages.push({
        role: 'assistant',
        content: firstChoice.message.content || null,
        tool_calls: firstChoice.message.tool_calls.map(tc => ({
          id: tc.id,
          type: tc.type,
          function: {
            name: tc.function.name,
            arguments: tc.function.arguments
          }
        }))
      });

      messages.push({
        role: 'tool',
        tool_call_id: toolCall.id,
        content: typeof toolResult === 'string' ? toolResult : JSON.stringify(toolResult)
      });

      const secondData = await litellmChat({ model: 'portfolio-default', messages });
      const botReply = secondData.choices[0].message.content;
      await redisClient.set(message, botReply, { EX: 3600 });
      return res.json({ botResponse: botReply });
    }

    // No tool call — direct response
    const botReply = firstChoice.message.content;
    await redisClient.set(message, botReply, { EX: 3600 });
    return res.json({ botResponse: botReply });

  } catch (error) {
    console.error('Error interacting with LiteLLM:', error.message);
    sendDiscordAlert(error, message).catch(e =>
      console.error("Failed to send Discord alert:", e.message));
    res.status(500).json({ error: 'Something went wrong' });
  }
});

// ✅ Health check endpoint
app.get('/health', (req, res) => {
  res.status(200).json({ status: 'ok' });
});

app.listen(port, '0.0.0.0', () => {
  console.log(`Server running on port ${port}`);
});