# Web Development & Python Backend Journey 🚀

Personal repository documenting my step-by-step developer journey—from foundational HTML, CSS, and modern JavaScript to building full RESTful APIs and server-rendered applications with **Flask** and **FastAPI**.

All projects and lessons are managed with clean virtual environments using modern Python tooling (`uv`).

---

## 📚 Table of Contents

1. [Frontend Fundamentals (HTML / CSS / JS)](#-frontend-fundamentals)
2. [Flask Backend & Jinja2](#-flask-backend-learn-flask)
3. [FastAPI Modern APIs & Pydantic](#-fastapi-modern-apis-learn-fastapi)
4. [Project Structure](#-project-structure)
5. [Getting Started](#-getting-started)
6. [Roadmap & What's Next](#-roadmap--whats-next)

---

## 🎨 Frontend Fundamentals

### 1. HTML (`HTML/`)
* [`index.html`](HTML/index.html) — First webpage with bio, favorite movies list, and weekly study routine table.
* [`form.html`](HTML/form.html) — Form inputs practice: text, email, password, date, radio buttons, checkboxes, dropdowns, and textarea.
* [`tags_practice.html`](HTML/tags_practice.html) — Exploring semantic tags: `<details>` / `<summary>`, `<progress>`, `<meter>`, image alt tags, and button alerts.

### 2. CSS (`CSS/`)
* [`index.html`](CSS/index.html) & [`style.css`](CSS/style.css) — CSS fundamentals, typography, button hover states, and visual box model comparisons (margin vs padding).
* [`flexbox.html`](CSS/flexbox.html) & [`flexbox.css`](CSS/flexbox.css) — Responsive horizontal navbar with `space-between` and flex cards with mobile media queries (`@media (max-width: 680px)`).
* [`grid.html`](CSS/grid.html) & [`grid.css`](CSS/grid.css) — Responsive card gallery using CSS Grid `repeat(auto-fit, minmax(280px, 1fr))`, CSS variables, and hover lift transitions.

### 3. JavaScript (`JS/`)
* [`index.html`](JS/index.html) & [`basics.js`](JS/basics.js) — Core JS foundations: variables (`let`/`const`), functions & arrow functions, `if/else`, loops, arrays (`.map()`, `.filter()`), and objects.
* [`dom.html`](JS/dom.html), [`dom.css`](JS/dom.css) & [`dom.js`](JS/dom.js) — Interactive DOM playground:
  - Counter with positive/negative color feedback
  - Dark mode / Light mode theme switcher
  - Real-time keystroke character counter
  - Dynamic item list with click-to-delete

---

## 🌶️ Flask Backend (`Learn-Flask/`)

Foundational Python backend learning covering routing, server-rendered templates, and REST APIs.

* **Core Features Built**:
  - Route handlers & URL parameters (`/user/<username>`, `/user/<int:id>`)
  - Server-side template rendering with **Jinja2** (`templates/index.html`)
  - Data validation using **Pydantic** (`User` model in `models.py`)
  - In-memory CRUD user management: GET all users, GET user by ID with 404 error handling
  - POST registration route parsing JSON bodies with status code 201

### Quick Run:
```bash
cd Learn-Flask
uv run python main.py
```
Visit: `http://127.0.0.1:5000`

---

## ⚡ FastAPI Modern APIs (`Learn-FastApi/`)

High-performance async web framework utilizing Python type hints and automatic OpenAPI documentation.

* **Core Features Built**:
  - Automatic Swagger documentation at `/docs` and ReDoc at `/redoc`
  - Strict input validation using Pydantic schemas (`PostCreate`)
  - Query parameter filtering (`/posts?search=FastAPI`) and path parameters (`/posts/{id}`)
  - Server-Sent Jinja2 dynamic rendering (`Templates/home.html`)
  - Full CRUD operations: GET all, GET single (with `HTTPException` 404), POST new post (201 Created), and DELETE post
  - Automated Python test script (`test_api.py`)

### Quick Run:
```bash
cd Learn-FastApi
uv run uvicorn main:app --reload
```
Visit Swagger UI: `http://127.0.0.1:8000/docs`  
Visit Dynamic Blog: `http://127.0.0.1:8000/home`

---

## 📂 Project Structure

```
WEBDEV/
├── HTML/                    # Semantic HTML & Form exercises
│   ├── index.html
│   ├── form.html
│   └── tags_practice.html
├── CSS/                     # Box Model, Flexbox & CSS Grid
│   ├── index.html / style.css
│   ├── flexbox.html / flexbox.css
│   └── grid.html / grid.css
├── JS/                      # JavaScript syntax & DOM manipulation
│   ├── index.html / basics.js
│   └── dom.html / dom.css / dom.js
├── Learn-Flask/             # Flask Backend practice
│   ├── main.py
│   ├── models.py
│   ├── templates/index.html
│   ├── pyproject.toml / uv.lock
│   └── README.md
├── Learn-FastApi/           # FastAPI REST API & Jinja2
│   ├── main.py
│   ├── Templates/home.html
│   ├── test_api.py
│   ├── pyproject.toml / uv.lock
│   └── README.md
└── README.md                # Master documentation
```

---

## 🛠️ Getting Started

### Prerequisites
* [uv](https://docs.astral.sh/uv/) (fast Python package and project manager)
* A modern web browser

### Running Frontend
Open any `.html` file inside `HTML/`, `CSS/`, or `JS/` directly in your browser or with VS Code Live Server.

### Running Backends
```bash
# To run Flask:
cd Learn-Flask
uv run python main.py

# To run FastAPI:
cd ../Learn-FastApi
uv run uvicorn main:app --reload
```

---

## 🎯 Roadmap & What's Next

- [x] HTML5 Semantics, Tables, and Forms
- [x] CSS Box Model, Flexbox layouts, and Grid galleries
- [x] JavaScript DOM manipulation, events, and array methods
- [x] Flask routing, Jinja2 templates, and REST endpoints
- [x] FastAPI async endpoints, Pydantic validation, and Swagger docs
- [ ] Database integration with PostgreSQL & SQLAlchemy
- [ ] Authentication with JWT & OAuth2
- [ ] Generative AI integration (LLM streaming, function calling, agents)
