#!/usr/bin/node
const http = require('http');
const fs = require('fs');

const countStudents = (filePath) => {
  return new Promise((resolve, reject) => {
    fs.readFile(filePath, 'utf8', (error, content) => {
      if (error) {
        reject(new Error('Cannot load the database'));
        return;
      }

      const lines = content.trim().split('\n');
      const studentLines = lines.slice(1).filter((line) => line.trim() !== '');
      const total = studentLines.length;

      const summary = {};
      for (const student of studentLines) {
        const parts = student.split(',');
        const name = parts[0];
        const field = parts[3];

        if (!summary[field]) summary[field] = [];
        summary[field].push(name);
      }

      let result = `Number of students: ${total}`;
      for (const field in summary) {
        const names = summary[field];
        result += `\nNumber of students in ${field}: ${names.length}. List: ${names.join(', ')}`;
      }

      resolve(result);
    });
  });
};

const database = process.argv[2];

const app = http.createServer(async function (req, res) {
  res.setHeader('Content-Type', 'text/plain');

  if (req.url === '/') {
    res.statusCode = 200;
    res.end('Hello Holberton School!');
  } else if (req.url === '/students') {
    if (!database) {
      res.statusCode = 500;
      res.end('Database filename not provided');
      return;
    }

    try {
      const output = await countStudents(database);
      res.statusCode = 200;
      res.end(`This is the list of our students\n${output}`);
    } catch (err)
