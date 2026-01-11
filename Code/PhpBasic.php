<!-- 

PHP IMP

PHP:Introduction and basic syntax of PHP, decision and looping with examples, PHP and HTML,Arrays,
Functions, Browser control and detection, string, Form processing, Files, AdvanceFeatures: Cookies and
Sessions, Object Oriented Programming with PHP.


 -->

<!-- PHP Syntax -->

<<?php 
echo "Hello World";
 ?>

<?php 

// verable

$Name = 'Shashank'

// Conditions  ------------------------------------------------------------------------------------

if ($age > 18) {
    echo "Adult";
}


if ($marks >= 40) {
    echo "Pass";
} else {
    echo "Fail";
}


if ($n == 1) {
    echo "One";
} elseif ($n == 2) {
    echo "Two";
} else {
    echo "Other";
}


switch ($day) {
    case 1: echo "Sunday"; break;
    case 2: echo "Monday"; break;
    default: echo "Invalid";
}


// PHP Loops  -------------------------------------------------------------------------------------

// While Loop
$i = 1;
while ($i <= 5) {
    echo $i;
    $i++;
}


// Do While Loop
$i = 1;
do {
    echo $i;
    $i++;
} while ($i <= 5);


// For Loop
for ($i = 1; $i <= 5; $i++) {
    echo $i;
}


// For Each Loop
foreach ($colors as $c) {
    echo $c;
}


// PHP array  -------------------------------------------------------------------------------------

// Indexed Array (List in python)
$colors = array("Red", "Green", "Blue");
echo $colors[0];


// Multidimensional Array (Multidimensional Array in python)
$marks = array(
    array(90, 80, 70),
    array(85, 75, 65)
);


// Associative Array (Dictionary in python)
$student = array("name" => "Shashank", "age" => 21);
echo $student["name"];


// Function in PHP  -------------------------------------------------------------------------------

// User-defined function
function greet() {
    echo "Hello Shashank!";
}
greet();



// Function with parameters
function add($a, $b) {
    return $a + $b;
}
echo add(5, 10);


// Function with default values
function welcome($name="User") {
    echo "Hello $name";
}
welcome();             // Output: Hello User
welcome("Shashank");   // Output: Hello Shashank

 ?>