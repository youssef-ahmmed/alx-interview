#!/usr/bin/node
const request = require('request');
const args = process.argv;

const getCharacters = (movieId) => {
  const url = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;
  request({url, json: true}, (error, response, body) => {
    if (error) {
      console.error('Error:', error);
      return;
    }
    const characters_urls = body.characters;
    for (const character_url of characters_urls) {
      getCharacterNames(character_url);
    }
  });
};

const getCharacterNames = (character_url) => {
  request(character_url, (error, response, body) => {
    if (error) {
      console.error('Error:', error);
    }
    console.log(JSON.parse(body).name);
  });
};


const movieId = args[2];
getCharacters(movieId);
