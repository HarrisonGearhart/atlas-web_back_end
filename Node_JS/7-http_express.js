#!/usr/bin/node
const express = require('express');
const fs = require('fs');

const countStudents = (filePath) => {
  return new Promise((resolve, reject) => {
    fs.readFile(filePath, 'utf8', (error, content) => {
      if (error) {
        reject(new Error('Cannot load the database'));
        return;
      }

      const lines = content.trim().split('\n');
      const studentData = lines.slice(1).filter(line => line.trim() !== '');

      const groupMap = {};
      let result = `Number of students: ${studentData.length}\n`;

      studentData.forEach(row => {
        const [name, , , field] = row.split(',');
        if (!groupMap[field]) {
          groupMap[field] = [];
        }
        groupMap[field].push(name);
      });

      Object.keys(groupMap).forEach(field => {
        const list = groupMap[field];
        result += `Number of students in ${field}: ${list.length}. List: ${list.join(', ')}\n`;
      });

      resolve(result.trim());
    });
  });
};

const dbPath = process.argv[2];
const app = express();

app.get('/', (req, res) => {
  res.set('Content-Type', 'text/plain');
  res.send('Hello Holberton School!');
});

app.get('/students', async (req, res) => {
  if (!dbPath) {
    res.status(500).type('text/plain').send('Database filename not provided');
    return;
  }

  try {
    const output = await countStudents(dbPath);
    res.type('text/plain').send(`This is the list of our students\n${output}`);
  } catch (err) {
    res.status(500).type('text/plain').send(err.message);
  }
});

app.listen(1245);

module.exports = app;
