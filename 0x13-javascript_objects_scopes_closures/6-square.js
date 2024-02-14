#!/usr/bin/node

const Rectangle = require('./4-rectangle');

class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    if (c) {
      for (let h = 0; h < this.width; h++) {
        let line = '';
        for (let w = 0; w < this.width; w++) {
          line += c;
        }
        console.log(line);
      }
    } else {
      super.print();
    }
  }
}

module.exports = Square;
