#!/usr/bin/node

/* import the modules */
const request = require('request');

/* declare constants */
const URL_FILM = 'https://swapi-api.alx-tools.com/api/films/';
const URL_PEOPLE = 'https://swapi-api.alx-tools.com/api/people/';
const MOVIE_ID = 3;

/* retrieve film */
request(URL_FILM, { json: true }, (err, res, body) => {
  if (err) {
    throw err;
  }
  const charactersUrls = body.results[MOVIE_ID - 1].characters;
  const actorsList = [];
  for (let i = 0; i < charactersUrls.length; i++) {
    /* break people url into parts using / as delimeter */
    const urlFields = charactersUrls[i].split('/');

    /* retrieve the actor ID from url */
    const actorId = parseInt(urlFields[urlFields.length - 2]);

    /* store the ids of all actors in an array */
    actorsList.push(actorId);
  }

  /* retrieve the names of the actors */
  request(URL_PEOPLE, { json: true }, (err, res, body) => {
    if (err) {
      throw err;
    }

    for (let i = 0; i < actorsList.length; i++) {
      const index = actorsList[i];
      console.log(body.results[index - 1].name);
    }
  });
});
