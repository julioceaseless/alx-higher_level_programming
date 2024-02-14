#!/usr/bin/node

const Rectangle = require('./5-square');

class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }
    for (let h = 0; h < this.width; h++) {
      let line = '';
      for (let w = 0; w < this.width; w++) {
        line += c;
      }
      console.log(line);
    }
  }
}

module.exports = Square;
