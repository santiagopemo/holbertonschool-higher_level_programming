#!/usr/bin/node
const args = process.argv;
if (args.length <= 3) {
  console.log(0);
} else {
  const sArgs = args.slice(2).map(Number);
  sArgs.sort();
  console.log(sArgs[sArgs.length - 2]);
}
