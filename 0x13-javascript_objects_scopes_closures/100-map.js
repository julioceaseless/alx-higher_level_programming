#!/usr/bin/node

const list = require('./100-data').list;

const newList = list.map(function (element) {
  return element * list.indexOf(element);
});
console.log(list);
console.log(newList);
