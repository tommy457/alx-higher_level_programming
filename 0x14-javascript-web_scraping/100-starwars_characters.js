#!/usr/bin/node

const request = require('request');
const filmId = process.argv[2];
const endpoint = `https://swapi-api.alx-tools.com/api/films/${filmId}/`;

request(endpoint, function (err, response, body) {
  if (err) {
    console.log(err);
  } else {
    const films = JSON.parse(body);
    const filmCharacters = films.characters;
    for (const film in filmCharacters) {
      request(filmCharacters[film], function (err, response, body) {
        if (err) {
          console.log(err);
        } else {
          const actors = JSON.parse(body);
          console.log(actors.name);
        }
      });
    }
  }
});
