# Learn Flask 🌶️

Practice workspace for learning Flask backend development with Python.

## Setup & Running with uv

```bash
# install dependencies & run
uv run python main.py
```

Server runs on `http://127.0.0.1:5000`.

## Endpoints

* `GET /` — Basic health/welcome message
* `GET /about` — Project about info
* `GET /home` — HTML rendered via Jinja2 template
* `GET /user/<username>` — Dynamic string route parameter
* `GET /users` — List all registered users
* `GET /user/<id>` — Lookup user by ID (returns 404 if not found)
* `POST /register` — Register a new user via JSON payload (returns 201)
