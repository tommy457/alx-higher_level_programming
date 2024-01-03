#!/usr/bin/node

const request = require('request');
const url = process.argv[2];

request(url, function (err, response, body) {
  if (err) {
    console.log(err);
  } else {
    const tasks = JSON.parse(body);
    const completedTasks = {};
    for (const task in tasks) {
      if (tasks[task].completed) {
        completedTasks[tasks[task].userId] = completedTasks[tasks[task].userId] ? completedTasks[tasks[task].userId] + 1 : 1;
      }
    }
    console.log(completedTasks);
  }
});
