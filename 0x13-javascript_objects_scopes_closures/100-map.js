#!/usr/bin/node
let i = 0;
const array1 = require('./100-data.js').list;
const array2 = array1.map((x) => x * i++);

console.log(array1);
console.log(array2);
