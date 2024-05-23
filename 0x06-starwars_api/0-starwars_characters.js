#!/usr/bin/node
/**
 * Prints all characters of a Star Wars movie.
 * The first positional argument passed is the Movie ID 
 * Display one character name per line in the same order
 * as the “characters” list in the /films/ endpoint.
 */

const request = require('request');
const filmId = process.argv[2];
const filmUrl = `https://swapi-api.alx-tools.com/api/films/${filmId}/`;

// Request API
request(filmUrl, async (err, res, body) => {
  if (err) {
    console.error(err);
    return;
  }
  if (res.statusCode !== 200) {
    console.error(`Failed to fetch film: ${res.statusCode}`);
    return;
  }

  // Find URLs of each character in the film
  const charUrlList = JSON.parse(body).characters;

  // Use URL list to character pages
  for (const charUrl of charUrlList) {
    await new Promise((resolve, reject) => {
      request(charUrl, (err, res, body) => {
        if (err) {
          console.error(err);
          reject(err);
          return;
        }
        if (res.statusCode !== 200) {
          console.error(`Failed to fetch character: ${res.statusCode}`);
          reject(new Error(`Failed to fetch character: ${res.statusCode}`));
          return;
        }

        // Find each character name and print in URL order
        console.log(JSON.parse(body).name);
        resolve();
      });
    });
  }
});
