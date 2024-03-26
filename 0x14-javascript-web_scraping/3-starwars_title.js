#!/usr/bin/node

const request = require('request');

const query = parseInt(process.argv[2]);
const url = 'https://swapi-api.alx-tools.com/api/films/';

request(url, { json: true }, function (err, response, body) {
  if (err) {
    throw (err);
  }
  for (let i = 0; i < body.results.length; i++) {
    if (body.results[i].episode_id === query) {
      console.log(body.results[i].title);
      break;
    }
  }
});
