#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let h = 0; h < this.height; h++) {
      let line = '';
      for (let w = 0; w < this.width; w++) {
        line += 'X';
      }
      console.log(line);
    }
  }

  double () {
    this.height *= 2;
    this.width *= 2;
  }

  rotate () {
    [this.height, this.width] = [this.width, this.height];
  }
}
module.exports = Rectangle;
