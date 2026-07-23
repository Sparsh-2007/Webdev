// JavaScript basics practice
console.log("Script loaded successfully!");

// Variables
let name = "Sparsh";
const currentYear = 2026;
let isCoding = true;

console.log("Name:", name);
console.log("Year:", currentYear);

// Functions
function add(a, b) {
  return a + b;
}

const multiply = (x, y) => x * y;

console.log("5 + 10 =", add(5, 10));
console.log("4 * 3 =", multiply(4, 3));

// Conditionals
let age = 19;
if (age >= 18) {
  console.log("Eligible to vote");
} else {
  console.log("Not eligible");
}

// Arrays
let languages = ["HTML", "CSS", "JavaScript"];
languages.push("Python");
console.log("My languages:", languages);

// Array map & filter
let numbers = [1, 2, 3, 4, 5, 6];
let doubled = numbers.map(n => n * 2);
let evenOnly = numbers.filter(n => n % 2 === 0);

console.log("Doubled:", doubled);
console.log("Evens:", evenOnly);

// Simple object
let user = {
  username: "sparsh07",
  role: "Developer",
  isOnline: true
};
console.log("User profile:", user);

function testAlert() {
  alert("External JS is working fine!");
}
