// axiosMock.js
const axios = require('axios');
const MockAdapter = require('axios-mock-adapter');

// Create a mock instance
const mock = new MockAdapter(axios, { delayResponse: 100 });

// Mock the OpenRouter API endpoint
mock.onPost('https://openrouter.ai/api/v1/chat/completions').reply(200, {
  choices: [
    {
      message: { content: "This is a mocked response from OpenRouter ✅" }
    }
  ]
});

console.log("Axios mock active (NODE_ENV=test)");
