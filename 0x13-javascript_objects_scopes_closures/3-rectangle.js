#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if ((w > 0) && (h > 0)) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let j = 0; j < this.height; j++) {
      let space = '';
      for (let k = 0; k < this.width; k++) {
        space += 'X';
      }
      console.log(space);
    }
  }
}

module.exports = Rectangle;
