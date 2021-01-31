const fs = require('fs')
const input = fs.readFileSync('/dev/stdin').toString().split('\n')

let a = Number(input[0])
let b = Number(input[1])
let hun = ~~(b/100)
let ten = ~~((b%100)/10)
let one = b%10

console.log(a * one)
console.log(a * ten)
console.log(a * hun)
console.log(a * b)