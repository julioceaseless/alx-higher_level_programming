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
      let line = 'X';
      for (let w = 0; w < this.width - 1; w++) {
        line += 'X';
      }
      console.log(line);
    }
  }
}
module.exports = Rectangle;
