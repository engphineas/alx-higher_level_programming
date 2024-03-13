#!/usr/bin/node
let num_arg = 0;

exports.logMe = function (item) {
  console.log(num_arg + ': ' + item);
  num_arg++;
};
