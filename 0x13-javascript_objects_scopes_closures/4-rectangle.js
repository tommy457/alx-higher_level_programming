#!/usr/bin/node

module.exports = class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    let rectangle = '';
    for (let j = 0; j < this.height; j++) {
      for (let i = 0; i < this.width; i++) {
        rectangle += 'X';
      }
      if (j < this.height - 1) {
        rectangle += '\n';
      }
    }
    console.log(rectangle);
  }

  rotate () {
    const tmp = this.width;
    this.width = this.height;
    this.height = tmp;
  }

  double () {
    this.height *= 2;
    this.width *= 2;
  }
};
