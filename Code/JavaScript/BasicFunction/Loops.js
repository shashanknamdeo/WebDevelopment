/*
for Loop
while Loop
do-while Loop
for-in Loop
for-of Loop
Labeled Statement
Break Statement
Continue Statement
Infinite Loop (Loop Error)
*/

// for Loop

let x;

// for loop begins when x = 2
// and runs till x <= 4
for (x = 2; x <= 4; x++) {
    console.log("Value of x: " + x);
}


// while Loop

let val = 1;

while (val < 6) {
    console.log(val); 
    val += 1;
}


// do-while Loop

let test = 1;

do {
    console.log(test);
    test++;
} while(test <= 5)


// for-in Loop

let myObj = { x: 1, y: 2, z: 3 };
for (let key in myObj) {
    console.log(key, myObj[key]);
}


// for-of Loop

let arr = [1, 2, 3, 4, 5];
for (let value of arr) {
    console.log(value);
}


// Labeled Statement (Similar to two nasted loop)

let sum = 0, a = 1; 

    // Label for outer loop 
outerloop: while (true) { 
    a = 1; 

    // Label for inner loop 
    innerloop: while (a < 3) { 
        sum += a; 
        if (sum > 12) { 

            // Break outer loop from inner loop 
            break outerloop; 
        } 
        console.log("sum = " + sum); 
        a++; 
    } 
}


// Break Statement

for (let i = 1; i < 6; i++) {
    if (i == 4) 
        break;
        
    console.log(i);
}


// Continue Statement

for (let i = 0; i < 11; i++) {
    if (i % 2 == 0) 
        continue;
        
    console.log(i);
}


// Infinite Loop (Loop Error)

    // condition should have been i>0.
for (let i = 5; i != 0; i -= 2) {
    console.log(i);
}

let x = 5;

    // Infinite loop because update statement is not provided
while (x == 5) {
    console.log("In the loop");
}