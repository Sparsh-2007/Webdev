from fastapi import FastAPI, Request, HTTPException, status
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel

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

class PostCreate(BaseModel):
    title: str
    content: str

@app.get("/html", response_class=HTMLResponse)
def read_root():
    return "<h1>hello world</h1>"

@app.get('/home')
def new(request: Request):
    return template.TemplateResponse(request, "home.html", {
        'posts': posts
    })

@app.get("/items")
def read_items(skip: int = 0, limit: int = 10, search: str | None = None):
    return {"skip": skip, "limit": limit, "search": search}

@app.get("/posts/{post_id}")
def get_post(post_id: int):
    for post in posts:
        if post["id"] == post_id:
            return post
    raise HTTPException(status_code=404, detail="Post not found")

@app.post("/posts", status_code=status.HTTP_201_CREATED)
def create_post(post_data: PostCreate):
    new_id = len(posts) + 1
    new_post = {
        "id": new_id,
        "title": post_data.title,
        "content": post_data.content
    }
    posts.append(new_post)
    return {"message": "Post created successfully", "post": new_post}
