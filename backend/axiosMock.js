// axiosMock.js
const axios = require('axios');
const MockAdapter = require('axios-mock-adapter');

const mock = new MockAdapter(axios, { delayResponse: 100 });

// Note: LiteLLM calls now use native fetch (not axios)
// so we don't need to mock them here anymore.
// The fetch mock is handled in server.js when NODE_ENV=test.

// Keep this in case any other axios calls are added in future
mock.onAny().passThrough();

console.log("Axios mock active (NODE_ENV=test)");