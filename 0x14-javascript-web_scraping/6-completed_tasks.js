#!/usr/bin/node

const request = require('request');

const URL = process.argv[2];

request(URL, { json: true }, function (err, response, body) {
  if (err) {
    throw (err);
  }
  const data = body;
  const tasks = {};

  /* retrieve data */
  data.forEach(task => {
    if (task.completed) {
      if (tasks[task.userId]) {
        tasks[task.userId]++;
      } else {
        tasks[task.userId] = 1;
      }
    }
  });
  console.log(tasks);
});
