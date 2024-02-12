#!/usr/bin/node

const size = parseInt(process.argv[2]);

if (size) {
  for (let h = 0; h < size; h++) {
    let line = 'X';
    for (let l = 0; l < size - 1; l++) {
      line += 'X';
    }
    console.log(line);
  }
} else {
  console.log('Missing size');
}
