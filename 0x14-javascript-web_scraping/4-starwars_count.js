#!/usr/bin/node

const request = require('request');

const URL = process.argv[2];
const ACTORID = 18;
let count = 0;

request(URL, { json: true }, function (err, response, body) {
  if (err) {
    throw (err);
  }
  const resultsList = body.results;
  /* retrieve list of actors */
  for (let i = 0; i < resultsList.length; i++) {
    for (let j = 0; j < resultsList[i].characters.length; j++) {
      if (resultsList[i].characters[j].indexOf(ACTORID) !== -1) {
        count++;
      }
    }
  }
  console.log(count);
});
