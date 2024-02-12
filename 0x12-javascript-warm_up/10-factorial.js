#!/usr/bin/node

const n = parseInt(process.argv[2]);

if (n) {
  console.log(factorial(n));
} else {
  console.log(1);
}

function factorial (n) {
  if (n === 1) {
    return 1;
  }
  const result = n * factorial(n - 1);
  return (result);
}
