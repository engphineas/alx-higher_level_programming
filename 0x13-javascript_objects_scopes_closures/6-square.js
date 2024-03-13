#!/usr/bin/node
const SquareP = require('./5-square');

class Square extends SquareP {
  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }
    for (let j = 0; j < this.height; j++) {
      let space = '';
      for (let k = 0; k < this.width; k++) {
        space += c;
      }
      console.log(space);
    }
  }
}

module.exports = Square;
