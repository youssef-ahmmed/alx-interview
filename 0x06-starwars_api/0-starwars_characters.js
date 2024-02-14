#!/usr/bin/node
const request = require('request');
const args = process.argv;

const getCharacters = (movieId) => {
  const url = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;
  request({ url, json: true }, (error, response, body) => {
    if (error) {
      console.error('Error:', error);
      return;
    }
    const charactersUrls = body.characters;
    for (const characterUrl of charactersUrls) {
      getCharacterNames(characterUrl);
    }
  });
};

const getCharacterNames = (characterUrl) => {
  request(characterUrl, (error, response, body) => {
    if (error) {
      console.error('Error:', error);
    }
    console.log(JSON.parse(body).name);
  });
};

const movieId = args[2];
getCharacters(movieId);
