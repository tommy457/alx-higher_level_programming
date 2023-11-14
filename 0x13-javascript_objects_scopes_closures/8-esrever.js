#!/usr/bin/node

exports.esrever = function (list) {
  const reversedList = [];

  for (let i = 0; i < list.length; i++) {
    reversedList[i] = list[list.length - i - 1];
  }
  return reversedList;
};
