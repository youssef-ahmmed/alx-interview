#!/usr/bin/node

const request = require('request');
const args = process.argv;

const getCharacters = (movieId) => {
  const url = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;

  request({ url, json: true }, async (error, response, body) => {
    if (error) {
      console.error('Error:', error);
      return;
    }

    const charactersUrls = body.characters;

    for (const characterUrl of charactersUrls) {
      const characterBody = await getCharacterBody(characterUrl);
      console.log(JSON.parse(characterBody).name);
    }
  });
};

async function getCharacterBody (characterUrl) {
  return new Promise((resolve, reject) => {
    request(characterUrl, (error, response, body) => {
      if (error) {
        reject(error);
      }
      if (response.statusCode === 200) {
        resolve(body);
      }
    });
  });
}

const movieId = args[2];
getCharacters(movieId);
