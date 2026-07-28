from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

template = Jinja2Templates(directory="Templates")

app = FastAPI()

posts = [
    {
        "id": 1,
        "title": "Getting Started with FastAPI",
        "content": "FastAPI is a modern, high-performance web framework for building APIs with Python based on standard type hints.",
    },
    {
        "id": 2,
        "title": "Understanding Jinja2 Templates",
        "content": "Jinja2 allows you to render dynamic HTML pages effortlessly by passing Python data directly into templates.",
    },
    {
        "id": 3,
        "title": "Mastering Async and Await in Python",
        "content": "Asynchronous programming lets your application handle thousands of concurrent requests efficiently without blocking.",
    },
    {
        "id": 4,
        "title": "Data Validation with Pydantic",
        "content": "Pydantic models ensure incoming request data is validated and typed correctly with automatic error messages.",
    },
]

@app.get("/html", response_class=HTMLResponse)
def read_root():
    return "<h1>hello world</h1>"

@app.get('/home')
def new(request: Request):
    return template.TemplateResponse(request, "home.html", {
        'posts': posts
    })
