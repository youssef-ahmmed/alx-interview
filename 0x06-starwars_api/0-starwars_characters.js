#!/usr/bin/node

const request = require('request');
const args = process.argv;

const movieId = args[2];
const url = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;

request.get(url, async (error, response, body) => {
  if (error) {
    console.error('Error:', error);
    return;
  }

  if (response.statusCode === 200) {
  const charactersUrls = JSON.parse(body).characters;

  for (const characterUrl of charactersUrls) {
    const characterBody = await getCharacterBody(characterUrl);
    console.log(JSON.parse(characterBody).name);
  }
  }
});

async function getCharacterBody (characterUrl) {
  return new Promise((resolve, reject) => {
    request.get(characterUrl, (error, response, body) => {
      if (error) {
        reject(error);
      }
      if (response.statusCode === 200) {
        resolve(body);
      }
    });
  });
}
