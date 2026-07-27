from flask import Flask, render_template
from models import User

app = Flask(__name__)

# sample in-memory users list
users = [
    User(id=1, name="Aman", username="aman123", email="aman@example.com", password="secretpassword"),
    User(id=2, name="Ram", username="ram_g", email="ram@example.com", password="rampassword")
]

@app.route("/")
def read_root():
    return {"message": "Hello World"}

@app.route("/about")
def about():
    return {"about": "Learning Flask - basic routing test"}

@app.route("/health")
def health():
    return {"status": "ok"}

@app.route("/home")
def home_page():
    topics = ["Routing & URL Parameters", "Jinja2 Templates", "Request Handling", "Pydantic Models"]
    return render_template("index.html", username="Sparsh", topics=topics)

@app.route("/user/<username>")
def get_username(username: str):
    return {"message": f"Hello, {username}!"}

@app.route("/user/<int:id>")
def get_user_id(id: int):
    for u in users:
        if u.id == id:
            return {"message": users}
    return {"message": "User not found"}

if __name__ == "__main__":
    app.run(debug=True)
