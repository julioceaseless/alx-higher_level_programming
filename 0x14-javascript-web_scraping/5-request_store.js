#!/usr/bin/node

const request = require('request');
const fs = require('fs');

const URL = process.argv[2];
const FILEPATH = process.argv[3];

request(URL, function (err, res, body) {
  if (err) {
    throw err;
  }
  const content = body;
  /* write web content to file */
  fs.writeFile(FILEPATH, content, (err) => {
    if (err) {
      throw err;
    }
  });
});
