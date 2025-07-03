#!/usr/bin/node
const fs = require('fs');

function countStudents(path) {
  fs.readFile(path, 'utf-8', (error, content) => {
    if (error) {
      throw new Error('Cannot load the database');
    }

    const lines = content.split('\n').filter(line => line.trim() !== '');
    const header = lines.shift(); // remove header

    const fieldGroups = {};
    let total = 0;

    lines.forEach((line) => {
      const parts = line.split(',');
      if (parts.length >= 4) {
        const firstName = parts[0];
        const field = parts[3];

        if (!fieldGroups[field]) {
          fieldGroups[field] = [];
        }

        fieldGroups[field].push(firstName);
        total += 1;
      }
    });

    console.log(`Number of students: ${total}`);

    Object.keys(fieldGroups).forEach((field) => {
      const students = fieldGroups[field];
      console.log(`Number of students in ${field}: ${students.length}. List: ${students.join(', ')}`);
    });
  });
}

module.exports = countStudents;
