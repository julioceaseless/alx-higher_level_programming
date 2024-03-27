#!/usr/bin/node

const request = require('request');

const movieId = parseInt(process.argv[2]);
const url = 'https://swapi-api.alx-tools.com/api/films/' + movieId;

request(url, { json: true }, function (err, response, body) {
  if (err) {
    throw (err);
  }
  console.log(body.title);
});
