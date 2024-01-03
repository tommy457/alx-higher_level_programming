#!/usr/bin/node

const request = require('request');
const endpoint = process.argv[2];

request(endpoint, function (err, response, body) {
  if (err) {
    console.log(err);
  } else {
    const films = JSON.parse(body);
    let count = 0;
    const filmList = films.results;

    for (const film in filmList) {
      const filmCharacters = filmList[film].characters;

      for (const character in filmCharacters) {
        if (filmCharacters[character].includes('18')) {
          count++;
        }
      }
    }
    console.log(count);
  }
});
