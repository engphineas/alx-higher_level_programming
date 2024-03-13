#!/usr/bin/node
exports.esrever = function (list) {
  let list_len = list.length - 1;
  let j = 0;
  while ((len - j) > 0) {
    const entry_arr = list[list_len];
    list[list_len] = list[j];
    list[j] = entry_arr;
    j++;
    list_len--;
  }
  return list;
};
