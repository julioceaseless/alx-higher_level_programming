#!/usr/bin/node

const fs = require('fs');

const f1 = process.argv[2];
const f2 = process.argv[3];
const f3 = process.argv[4];

let content = fs.readFileSync(f1, 'utf8');
content += fs.readFileSync(f2, 'utf8');
fs.writeFileSync(f3, content);
