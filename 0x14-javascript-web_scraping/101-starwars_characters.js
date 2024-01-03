#!/usr/bin/node

const request = require('request');
const filmId = process.argv[2];
const endpoint = `https://swapi-api.alx-tools.com/api/films/${filmId}/`;
const endpointActors = {};
let filmCharacters;

request(endpoint, function (err, response, body) {
  if (err) {
    console.log(err);
  } else {
    const films = JSON.parse(body);
    filmCharacters = films.characters;
    for (const film in filmCharacters) {
      request(filmCharacters[film], function (err, response, body) {
        if (err) {
          console.log(err);
        } else {
          const actors = JSON.parse(body);
          sortedData(film, actors.name);
        }
      });
    }
  }
});

function sortedData (endpoint, name) {
  endpointActors[endpoint] = name;
  if (Object.entries(endpointActors).length === filmCharacters.length) {
    for (const endpoint in filmCharacters) {
      console.log(endpointActors[endpoint]);
    }
  }
}
