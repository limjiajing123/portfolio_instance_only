// redis.js
const redis = require('redis');

const client = redis.createClient({ url: 'redis://redis:6379' }); // "redis" = Docker container name

client.connect()
  .then(() => console.log('✅ Redis connected'))
  .catch((err) => console.error('❌ Redis connection failed:', err));

module.exports = client;
