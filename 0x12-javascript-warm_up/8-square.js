#!/usr/bin/node
const size = parseInt(process.argv[2]);
let i;
let j = 0;
let square = '';

if (size) {
  while (j < size) {
    for (i = 0; i < size; i++) {
      square += 'X';
    }
    if (j < size - 1) {
      square += '\n';
    }
    j++;
  }
  console.log(square);
} else {
  console.log('Missing size');
}
