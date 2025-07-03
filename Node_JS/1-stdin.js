#!/usr/bin/node

process.stdout.write('Welcome to Atlas School, what is your name?\n');

process.stdin.on('data', (data) => {
  const name = data.toString();

  process.stdout.write(`Your name is: ${name}`);
  console.log('This important software is now closing');
  process.exit();
});
