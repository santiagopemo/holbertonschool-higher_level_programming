#!/usr/bin/node
const request = require('request');
const id = process.argv[2];
const url = 'https://swapi-api.hbtn.io/api/films/' + id;

request.get(url, (err, response, body) => {
  if (err) {
    console.log(err);
  } else {
    if (response.statusCode === 200) {
      const rJson = JSON.parse(body);
      console.log(rJson.title);
    }
  }
});
