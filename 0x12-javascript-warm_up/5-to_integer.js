#!/usr/bin/node
const myNum = parseInt(process.argv[2]);
if (myNum) {
  console.log('My number : %d', myNum);
} else {
  console.log('Not a number');
}
