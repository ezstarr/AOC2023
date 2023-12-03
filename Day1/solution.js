// const fs = require('fs');
// const readline = require('readline');

// const data = fs.readFileSync('input.txt', 'utf8').split('\n');
// console.log(data);

import { readFileSync } from 'fs';
import { parse } from 'path';

const INPUTS = readFileSync('sample.txt', { encoding: 'utf-8', flag: 'r'}).split('\r\n');

console.log(INPUTS)

let p1Total = 0

INPUTS.forEach(line => {
  let lineNum = ""

  for (let i=0; i < line.length; i++) {
    if (!isNaN(parseInt(line[i], 10))) { // NaN = Not a Number
      lineNum += line[i]
      break;
    }
  }
  for (let i = line.length - 1; i >= 0; i--) {
    if (!isNaN(parseInt(line[i], 10))) {
      lineNum += line[i]
      break;
    }
  }
  console.log(parseInt(lineNum, 10))
  p1Total += parseInt(lineNum, 10)
})
console.log(p1Total)