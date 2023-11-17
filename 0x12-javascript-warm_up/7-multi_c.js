#!/usr/bin/node
const myVar = 'C is fun';
let num = parseInt(process.argv[2]);

if (num) {
  while (num > 0) {
    console.log(myVar);
    num--;
  }
} else {
  console.log('Missing number of occurrences');
}
