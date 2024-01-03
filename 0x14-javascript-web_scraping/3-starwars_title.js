#!/usr/bin/node

const request = require('request');
const filmId = process.argv[2];
const endpoint = `https://swapi-api.alx-tools.com/api/films/${filmId}`;

request(endpoint, function (err, response, body) {
  if (err) {
    console.log(err);
  } else {
    console.log(JSON.parse(body).title);
  }
});
