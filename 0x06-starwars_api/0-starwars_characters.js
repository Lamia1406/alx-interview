#!/usr/bin/node
const request = require('request');

function fetch (url) {
  return new Promise((resolve, reject) => {
    request(url, { json: true }, (error, response, body) => {
      if (error) {
        reject(new Error(`Error fetching ${url}: ${error.message}`));
      } else if (response.statusCode !== 200) {
        reject(new Error(`Error: Received status code ${response.statusCode} for ${url}`));
      } else {
        resolve(body);
      }
    });
  });
}

if (process.argv[2] === undefined) {
  console.log('Please specify the movie ID');
  process.exit(1);
}

fetch(`https://swapi-api.alx-tools.com/api/films/${process.argv[2]}/`)
  .then(filmData => {
    const characterUrls = filmData.characters;

    if (!characterUrls || characterUrls.length === 0) {
      console.log('No characters found for this film.');
      return;
    }

    return Promise.all(characterUrls.map(url => fetch(url)));
  })
  .then(characters => {
    if (characters) {
      characters.forEach(character => console.log(character.name));
    }
  })
  .catch(error => {
    console.error(error);
  });
