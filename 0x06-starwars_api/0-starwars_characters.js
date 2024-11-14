#!/usr/bin/node
// Script to fetch and print names of characters from a specific Star Wars movie
// Usage: node script.js <movie_id>

const request = require('request');
const API_URL = 'https://swapi-api.hbtn.io/api';

if (process.argv.length > 2) {
  const movieID = process.argv[2];
  const movieURL = `${API_URL}/films/${movieID}/`;

  request(movieURL, (err, response, body) => {
    if (err) return console.log(err);

    const characterURLs = JSON.parse(body).characters;

    const characterPromises = characterURLs.map(
      url => new Promise((resolve, reject) => {
        request(url, (promiseErr, _, characterBody) => {
          if (promiseErr) return reject(promiseErr);

          resolve(JSON.parse(characterBody).name);
        });
      })
    );

    Promise.all(characterPromises)
      .then(names => console.log(names.join('\n')))
      .catch(promiseError => console.log(promiseError));
  });
}
