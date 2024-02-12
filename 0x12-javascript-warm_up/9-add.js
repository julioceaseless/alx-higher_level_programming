#!/usr/bin/node

const a = parseInt(process.argv[2]);
const b = parseInt(process.argv[3]);

const sum = add(a, b);
console.log(sum);

function add (a, b) {
  return a + b;
}
