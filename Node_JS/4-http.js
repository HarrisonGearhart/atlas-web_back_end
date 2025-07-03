#!/usr/bin/node
const http = require('http');

const app = http.createServer(function (req, res) {
  res.statusCode = 200;
  res.setHeader('Content-Type', 'text/plain');
  res.end('Hello Holberton School!');
});

app.listen(1245);

module.exports = app;
