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

// 3. Live Character Counter
const charInput = document.getElementById("charInput");
const charCount = document.getElementById("charCount");

charInput.addEventListener("input", (e) => {
  charCount.textContent = e.target.value.length;
});

// 4. Dynamic Item List
const itemInput = document.getElementById("itemInput");
const addItemBtn = document.getElementById("addItemBtn");
const itemList = document.getElementById("itemList");

function createListItem(text) {
  const li = document.createElement("li");
  li.innerHTML = `${text} <span class="delete-hint">&times;</span>`;
  li.title = "Click to remove";
  li.addEventListener("click", () => {
    li.remove();
  });
  return li;
}

// Add event listeners to initial items
itemList.querySelectorAll("li").forEach((li) => {
  li.title = "Click to remove";
  li.addEventListener("click", () => {
    li.remove();
  });
});

function handleAddItem() {
  const text = itemInput.value.trim();
  if (text !== "") {
    const newItem = createListItem(text);
    itemList.appendChild(newItem);
    itemInput.value = "";
    itemInput.focus();
  }
}

addItemBtn.addEventListener("click", handleAddItem);

itemInput.addEventListener("keydown", (e) => {
  if (e.key === "Enter") {
    handleAddItem();
  }
});
