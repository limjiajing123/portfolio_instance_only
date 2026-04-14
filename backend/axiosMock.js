// axiosMock.js
const axios = require('axios');
const MockAdapter = require('axios-mock-adapter');

const mock = new MockAdapter(axios, { delayResponse: 100 });

// Mock the LiteLLM endpoint (updated from OpenRouter)
mock.onPost('http://litellm:4000/chat/completions').reply(200, {
  choices: [
    {
      message: { content: "This is a mocked response from LiteLLM ✅" }
    }
  ]
});

console.log("Axios mock active (NODE_ENV=test)");