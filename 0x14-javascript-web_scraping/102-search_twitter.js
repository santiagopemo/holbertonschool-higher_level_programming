#!/usr/bin/node
const base64 = require('base-64');
const request = require('request');
const utf8 = require('utf8');
const apiUrl = 'https://api.twitter.com';
const key = process.argv[2];
const secret = process.argv[3];
const searchString = process.argv[4];
const bearerToken64 = base64.encode(utf8.encode(key) + ':' + utf8.encode(secret));
const options = {
  url: apiUrl + '/oauth2/token?grant_type=client_credentials',
  headers: {
    'User-Agent': 'My Twitter App',
    Authorization: 'Basic ' + bearerToken64,
    'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8'
  }
};
request.post(options, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    if (response.statusCode === 200) {
      const rJson = JSON.parse(body);
      const accesToken = rJson.access_token;
      const options = {
        url: apiUrl + '/1.1/search/tweets.json',
        headers: {
          'User-Agent': 'My Twitter App',
          Authorization: 'Bearer ' + accesToken
        },
        qs: {
          q: searchString,
          count: 5
        }
      };
      request.get(options, (error, response, body) => {
        if (error) {
          console.log(error);
        }
        const tweets = JSON.parse(body).statuses;
        for (const tweet of tweets) {
          console.log('[' + tweet.id + '] ' + tweet.text + ' by ' + tweet.user.name);
        }
      });
    }
  }
});
