www.geeksforgeeks.org/conditional-statements-in-javascript/

/*
if statement                Executes a block of code if a specified condition is true.
else statement              Executes a block of code if the same condition of the preceding if statement is false.
else if statement           Adds more conditions to the if statement, allowing for multiple alternative conditions to be tested.
switch statement            Evaluates an expression, then executes the case statement that matches the expression’s value.
ternary operator            Provides a concise way to write if-else statements in a single line.
Nested if else statement    Allows for multiple conditions to be checked in a hierarchical manner.
*/


// if statement     
// else statement   
// else if statement

const num = 0;

if (num > 0) {
    console.log("Given number is positive.");
} else if (num < 0) {
    console.log("Given number is negative.");
} else {
    console.log("Given number is zero.");
};


// switch statement

const marks = 85;

let Branch;

switch (true) {
    case marks >= 90:
        Branch = "Computer science engineering";
        break;
    case marks >= 80:
        Branch = "Mechanical engineering";
        break;
    case marks >= 70:
        Branch = "Chemical engineering";
        break;
    case marks >= 60:
        Branch = "Electronics and communication";
        break;
    case marks >= 50:
        Branch = "Civil engineering";
        break;
    default:
        Branch = "Bio technology";
        break;
}

console.log(`Student Branch name is : ${Branch}`);


// ternary operator

let age = 21;

const result =
    (age >= 18) ? "You are eligible to vote."
        : "You are not eligible to vote.";

console.log(result);


// Nested if else statement 

let weather = "sunny";
let temperature = 25;

if (weather === "sunny") {
    if (temperature > 30) {
        console.log("It's a hot day!");
    } else if (temperature > 20) {
        console.log("It's a warm day.");
    } else {
        console.log("It's a bit cool today.");
    }
} else if (weather === "rainy") {
    console.log("Don't forget your umbrella!");
} else {
    console.log("Check the weather forecast!");
};