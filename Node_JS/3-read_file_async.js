#!/usr/bin/node
const fs = require('fs');

function countStudents(path) {
  return new Promise((resolve, reject) => {
    fs.readFile(path, 'utf-8', (error, content) => {
      if (error) {
        reject(new Error('Cannot load the database'));
        return;
      }

      const rows = content.split('\n').filter(row => row.trim() !== '');
      const headers = rows[0];
      const dataRows = rows.slice(1);

      console.log(`Number of students: ${dataRows.length}`);

      const groupByField = {};

      dataRows.forEach((row) => {
        const columns = row.split(',');
        const name = columns[0];
        const field = columns[3];

        if (!groupByField[field]) {
          groupByField[field] = [];
        }

        groupByField[field].push(name);
      });

      for (const field of Object.keys(groupByField)) {
        const list = groupByField[field];
        console.log(`Number of students in ${field}: ${list.length}. List: ${list.join(', ')}`);
      }

      resolve();
    });
  });
}

module.exports = countStudents;
