
// JS is Dynamic language
// like python
// means a veriable can chage its datatype

// How JS exicutes

// Exicution Context
//  1. Memory Phase
//      In Memory Phase memory is alocated to function and veriable
//  2. Exicution Phase
//      In Exicution Phase code is exicuted line by line

// Hoisting
//  Because functon and veriable is in memory 
//      1. function can be call above the initlization of function
//      2. veriable "var" can also be call before define but return "Undefine" (not throw any error)


// var
//      for declare veriable
//      not recomonanded

var state = "Mp"

// let
//      for declare veriable

let sum = 20

// const
//      for declare constant

const add = 100


// Note:
//     let and const are BLOCK SCOPED, means if a const or let is define in a {} "Block" it is only excessible in {} "Block"


// ------------------------------------------------------------------------------------------------

// print
console.log("Hello World")

// ------------------------------------------------------------------------------------------------

// Verable

// Undefined veriable
let age
console.log(age)
console.log(typeof(age))

// Defined verable
let name = "Shashank"
console.log(name)
console.log(typeof(name))

// ------------------------------------------------------------------------------------------------

// Value types - similer to DataTypes in python

// string   - "akanncnakn"
// number   - 123 or 56.2
// Boolean  - true or false
// undefined - by default, should not assign it my us
// object - null
// symbol

// ------------------------------------------------------------------------------------------------

// Reference type

// Notes:
// typeof all Reference type is "object"

// Object - same as dict in python

let object = {student:"ram", class:12, subject:"PCM"}

console.log(typeof(object))

console.log(object.subject)
// or
console.log(object["subject"])


// Arrays

let arr = ["list", 1, 1.5, true, null, object]
console.log(arr)

// Function

function language(name) {
    console.log(name)
}

console.log(language("Python"))
console.log(language("JavaScript"))


// ------------------------------------------------------------------------------------------------

// Value types VS Reference type


// value types only copies value of verable

let x = "Shashank"
let y = x
x = "Ram"

console.log(x) // Ram
console.log(y) // Shashank


// Reference types copies reference location of verable

let a = {student:"Shashank", class:12, subject:"PCM"};
let b = a
a.student = "ram";


console.log(a) // { student: 'ram', class: 12, subject: 'PCM' }
console.log(b) // { student: 'ram', class: 12, subject: 'PCM' }


// ------------------------------------------------------------------------------------------------


// Functions

// Note:
//     A function can be pass in let, const, var or argument to other function

let summition = function (a, b) {
    return a + b
}

function demoFunction(argument, a, b) {
    console.log("argument : ", argument(a, b))
}

demoFunction(summition, 1, 9)


// Type of function in JS

// Regular function
function add(a, b) {
  return a + b;
}

// Arrow function
const add = (a, b) => {
  return a + b;
};

// Even shorter Arrow function (no need of return statement)
const add = (a, b) => a + b;






