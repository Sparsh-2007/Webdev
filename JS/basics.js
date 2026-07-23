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

function testAlert() {
  alert("External JS is working fine!");
}
