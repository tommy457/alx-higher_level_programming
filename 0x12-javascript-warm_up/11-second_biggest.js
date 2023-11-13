#!/usr/bin/node
if (process.argv.length <= 3) {
  console.log(0);
} else {
  const newArray = process.argv.slice(2).sort((a, b) => b - a);
  console.log(newArray[1]);
}
