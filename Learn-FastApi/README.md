# Learn FastAPI ⚡

Practice workspace for modern async Python APIs and Jinja2 templating using FastAPI.

## Setup & Running with uv

```bash
# start development server with reload
uv run uvicorn main:app --reload
```

* API server: `http://127.0.0.1:8000`
* Interactive Swagger Docs: `http://127.0.0.1:8000/docs`
* Alternative Redoc: `http://127.0.0.1:8000/redoc`

## Endpoints

* `GET /html` — Simple raw HTML response
* `GET /home` — Dynamic blog posts template rendered with Jinja2
* `GET /items` — Testing query parameters (`skip`, `limit`, `search`)
* `GET /posts` — List all posts (supports `?search=<keyword>`)
* `GET /posts/{id}` — Get single post by ID (404 HTTPException if missing)
* `POST /posts` — Create a new post via Pydantic schema validation (returns 201)
* `DELETE /posts/{id}` — Remove a post by ID
