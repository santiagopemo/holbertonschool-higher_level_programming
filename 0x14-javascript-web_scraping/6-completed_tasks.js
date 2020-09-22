#!/usr/bin/node
const request = require('request');
const url = process.argv[2];

request.get(url, (err, response, body) => {
  if (err) {
    console.log(err);
  } else if (response.statusCode === 200) {
    const newDict = {};
    const todos = JSON.parse(body);
    for (const task of todos) {
      const key = task.userId;
      if (!newDict[key]) {
        newDict[key] = 0;
      }
    }
    for (const task of todos) {
      if (task.completed) {
        const key = task.userId;
        newDict[key]++;
      }
    }
    console.log(newDict);
  }
});
