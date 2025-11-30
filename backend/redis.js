// redis.js
const redis = require('redis');

// Use env if provided, otherwise default to localhost (for local dev)
const REDIS_HOST = process.env.REDIS_HOST || 'localhost';
const REDIS_PORT = process.env.REDIS_PORT || 6379;

console.log(`🔌 Connecting to Redis at ${REDIS_HOST}:${REDIS_PORT}`);

const client = redis.createClient({
  url: `redis://${REDIS_HOST}:${REDIS_PORT}`,
});

client.connect()
  .then(() => console.log('✅ Redis connected'))
  .catch((err) => console.error('❌ Redis connection failed:', err));

module.exports = client;
