#!/usr/bin/node
const array1 = require('./100-data.js').list;
const array2 = array1.map((x) => x * 2);

console.log(array1);
console.log(array2);
