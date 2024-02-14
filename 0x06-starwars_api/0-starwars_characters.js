#!/usr/bin/node
const request = require('request');
const args = process.argv;

const movieId = args[2];
const url = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;

function printCharacters (characters, idx) {
  request(characters[idx], (error, response, body) => {
    if (error) {
      console.error(error);
    } else {
      console.log(JSON.parse(body).name);
      if (idx + 1 < characters.length) {
        printCharacters(characters, idx + 1);
      }
    }
  });
}

request(url, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    const characters = JSON.parse(body).characters;
    printCharacters(characters, 0);
  }
});
