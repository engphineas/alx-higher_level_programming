#!/usr/bin/node

exports.converter = function (base) {
  return function (num_base) {
    return num_base.toString(base);
  };
};
