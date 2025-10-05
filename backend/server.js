require('dotenv').config();

console.log("NODE_ENV =", process.env.NODE_ENV);

// ✅ Only patch axios mock; still start Express normally
if (process.env.NODE_ENV === "test") {
  console.log("Running in test mode: axios is mocked");
  require('./axiosMock');
}

const express = require('express');
const axios = require('axios');
const cors = require('cors');
const portfolioKnowledge = require('./portfolioKnowledge');
const redisClient = require('./redis'); // Import Redis client

const app = express();
const port = 5000;

const corsOptions = {
  origin: ['https://www.limjiajing.com'],  // Frontend domain
  methods: ['GET', 'POST', 'OPTIONS'],
  allowedHeaders: ['Content-Type', 'Authorization'],
  credentials: true,  // Allow credentials (cookies) to be sent
};

app.use(cors(corsOptions));  // Apply CORS options
// app.use(cors());
app.use(express.json());

// Debugging logs
console.log("Server starting...");
console.log("NODE_ENV:", process.env.NODE_ENV || "not set");
console.log("OpenRouter API Key:", process.env.OPENROUTER_API_KEY ? "Loaded" : "Not Found");

// Chatbot endpoint that handles user messages
app.post('/api/chat', async (req, res) => {
  const { message } = req.body;

  if (!message) {
    return res.status(400).json({ error: 'Message is required' });
  }

  const apiKey = process.env.OPENROUTER_API_KEY;
  if (!apiKey) {
    console.error("Missing OPENROUTER_API_KEY!");
    return res.status(500).json({ error: "Server misconfiguration: Missing API key" });
  }

  try {
    // Check Redis cache
    const cachedResponse = await redisClient.get(message);
    if (cachedResponse) {
      console.log('Returning cached response');
      return res.json({ botResponse: cachedResponse });
    }

    const response = await axios.post(
      'https://openrouter.ai/api/v1/chat/completions',
      {
        model: 'deepseek/deepseek-chat-v3.1:free', // Change to Deepseek R1
        messages: [
          {
            role: 'system',
            content: `You are an AI assistant helping users learn about Jia Jing's portfolio website. Use the following context to answer questions: ${portfolioKnowledge} Please give your answers in very short sentences and do not output your reasoning to getting the answers.`,
          },
          {
            role: 'user',
            content: message,
          },
        ],
      },
      {
        headers: {
          Authorization: `Bearer ${apiKey}`,
          'Content-Type': 'application/json',
          'HTTP-Referer': process.env.YOUR_SITE_URL || '',
          'X-Title': process.env.YOUR_SITE_NAME || '',
        },
      }
    );


    if (response.data.choices && response.data.choices.length > 0) {
      const botReply = response.data.choices[0].message.content;

      // Save to cache (expire in 1 hour)
      await redisClient.set(message, botReply, { EX: 3600 });

      return res.json({ botResponse: botReply });
    } else {
      return res.status(500).json({ error: 'No valid response from AI' });
    }
  } catch (error) {
    console.error('Error interacting with OpenRouter API:', error);
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
