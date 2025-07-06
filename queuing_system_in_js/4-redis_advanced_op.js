import { createClient, print } from 'redis';

const client = createClient();

client.on('connect', () => {
  console.log('Redis client connected to the server');
});

client.on('error', (err) => {
  console.log('Redis client not connected to the server:', err.toString());
});

// Key for the hash
const hashKey = 'HolbertonSchools';

// Values to set in the hash
client.hset(hashKey, 'Portland', 50, print);
client.hset(hashKey, 'Seattle', 80, print);
client.hset(hashKey, 'New York', 20, print);
client.hset(hashKey, 'Bogota', 20, print);
client.hset(hashKey, 'Cali', 40, print);
client.hset(hashKey, 'Paris', 2, print);

// Retrieve and display the hash
client.hgetall(hashKey, (err, reply) => {
  if (err) {
    console.error(err);
    return;
  }
  console.log(reply);
});

