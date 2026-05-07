const axios = require('axios');
const MockAdapter = require('axios-mock-adapter');

const mock = new MockAdapter(axios, { delayResponse: 100 });

// Mock MCP tools endpoint
mock.onGet('http://mcp-server:8000/tools').reply(200, {
  tools: [
    {
      name: 'get_contact',
      description: "Get Jia Jing's contact information",
      inputSchema: { type: 'object', properties: {} }
    }
  ]
});

// Mock MCP tool call
mock.onPost(/http:\/\/mcp-server:8000\/tools\/.*/).reply(200, {
  content: [{ text: '{"email": "limjiajing123@gmail.com"}' }]
});

// Mock LiteLLM — direct response (no tool call)
mock.onPost('http://litellm:4000/chat/completions').reply(200, {
  choices: [{
    finish_reason: 'stop',
    message: {
      content: 'This is a mocked response from LiteLLM ✅',
      tool_calls: null
    }
  }]
});

console.log("Axios mock active (NODE_ENV=test)");