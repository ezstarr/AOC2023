// AOC Day1, 2023, TS

import { readFileSync } from 'fs';
import { parse } from 'path';

const INPUT = readFileSync('sample.txt', { encoding: 'utf-8' }).split('\r\n');

let p1Total: number = 0;

INPUT.forEach((line: string) => {
  let lineNum: string = "";

  for (let i: number = 0; i < line.length; i++) {
    if (!isNaN(parseInt(line[i], 10))) {
      lineNum += line[i];
      break;
    }
  }
  for (let i: number = line.length; i >= 0; i--) {
    if(!isNaN(parseInt(line[i], 10))) {
      lineNum += line[i];
      break;
    }
  }
  p1Total += parseInt(lineNum, 10);
})
console.log(p1Total);