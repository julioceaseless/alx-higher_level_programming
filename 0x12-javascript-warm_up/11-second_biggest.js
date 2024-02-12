#!/usr/bin/node

const args = process.argv.slice(2);

if (args) {
  const argnums = toInt(args);
  if (argnums.length === 0) {
    console.log(0);
  } else if (argnums.length === 1) {
    console.log(1);
  } else {
    argnums.sort();
    console.log(secondLargest(argnums));
  }
}

function toInt (arr) {
  const argnums = [];
  for (let i = 0; i < arr.length; i++) {
    argnums[i] = parseInt(arr[i]);
  }
  return argnums;
}

function secondLargest (arr) {
  const len = arr.length;
  let i = len - 2;
  while (arr[i] >= arr[len - 1]) {
    i--;
  }
  return arr[i];
}
