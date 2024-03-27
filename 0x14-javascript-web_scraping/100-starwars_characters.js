#!/usr/bin/node

/* import the modules */
const request = require('request');

/* declare constants */
const URL_FILM = 'https://swapi-api.alx-tools.com/api/films/';
const MOVIE_ID = 3;

/* retrieve film */
request(URL_FILM, { json: true }, (err, res, body) => {
  if (err) {
    throw err;
  }
  const charactersUrls = body.results[MOVIE_ID - 1].characters;
  /*
   * NOT USEFUL
   * const actorsList = [];
   * for (let i = 0; i < charactersUrls.length; i++) {
   *   const urlFields = charactersUrls[i].split('/');
   *    const actorId = parseInt(urlFields[urlFields.length - 2]);
   *    actorsList.push(actorId);
   *    }
   */

  /* retrieve the names of the actors */
  charactersUrls.forEach((actorUrl) => {
    request(actorUrl, { json: true }, (err, res, body) => {
      if (err) {
        throw err;
      }
      console.log(body.name);
    });
  });
});
