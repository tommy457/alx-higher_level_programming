#!/usr/bin/node
const dict1 = require('./101-data.js').dict;
const dict2 = occurrences(dict1);
console.log(dict2);

function occurrences(dict) {
  let dict2 = {};
  for (const [key, value] of Object.entries(dict)) {
    if (!(value in dict2)) {
      dict2[value] = [];
      dict2[value].push(key);
    }
    else {
      dict2[value].push(key);
    }
  }
  return dict2;
};
