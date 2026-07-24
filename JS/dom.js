// Day 7: DOM Manipulation and Event Listeners

// 1. Counter Logic
let count = 0;
const counterDisplay = document.getElementById("counterValue");
const incrementBtn = document.getElementById("incrementBtn");
const decrementBtn = document.getElementById("decrementBtn");
const resetBtn = document.getElementById("resetBtn");

function updateCounterDisplay() {
  counterDisplay.textContent = count;
  if (count > 0) {
    counterDisplay.className = "positive";
  } else if (count < 0) {
    counterDisplay.className = "negative";
  } else {
    counterDisplay.className = "";
  }
}

incrementBtn.addEventListener("click", () => {
  count++;
  updateCounterDisplay();
});

decrementBtn.addEventListener("click", () => {
  count--;
  updateCounterDisplay();
});

resetBtn.addEventListener("click", () => {
  count = 0;
  updateCounterDisplay();
});

// 2. Dark Mode Toggle
const themeToggleBtn = document.getElementById("themeToggleBtn");
themeToggleBtn.addEventListener("click", () => {
  document.body.classList.toggle("dark-mode");
  const isDark = document.body.classList.contains("dark-mode");
  themeToggleBtn.textContent = isDark ? "☀️ Light Mode" : "🌙 Dark Mode";
});
