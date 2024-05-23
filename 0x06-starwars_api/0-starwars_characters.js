#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2];
if (!movieId) {
  console.error('Please provide a Movie ID');
  process.exit(1);
}

const url = `https://swapi.dev/api/films/${movieId}/`;

request(url, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }
  if (response.statusCode !== 200) {
    console.error(`Failed to fetch movie: ${response.statusCode}`);
    return;
  }

  const film = JSON.parse(body);
  const characters = film.characters;
  const charactersCount = characters.length;
  let charactersFetched = 0;

  characters.forEach(characterUrl => {
    request(characterUrl, (error, response, body) => {
      if (error) {
        console.error(error);
        return;
      }
      if (response.statusCode !== 200) {
        console.error(`Failed to fetch character: ${response.statusCode}`);
        return;
      }

      const character = JSON.parse(body);
      console.log(character.name);
      charactersFetched++;

      if (charactersFetched === charactersCount) {
        process.exit(0);
      }
    });
  });
});
