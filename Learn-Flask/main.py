from flask import Flask, render_template, request
from models import User

app = Flask(__name__)

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

@app.route("/users")
def get_all_users():
    return {"users": [u.model_dump() for u in users]}

@app.route("/user/<int:id>")
def get_user_id(id: int):
    for u in users:
        if u.id == id:
            return {"user": u.model_dump()}
    return {"error": "User not found"}, 404

@app.route("/register", methods=["POST"])
def register():
    data = request.get_json()
    if not data:
        return {"error": "Invalid JSON body"}, 400
    
    new_id = len(users) + 1
    try:
        new_user = User(
            id=new_id,
            name=data.get("name", ""),
            username=data.get("username", ""),
            email=data.get("email", ""),
            password=data.get("password", "")
        )
        users.append(new_user)
        return {"message": "User registered successfully", "user": new_user.model_dump()}, 201
    except Exception as e:
        return {"error": str(e)}, 400

@app.errorhandler(404)
def page_not_found(e):
    return {"error": "Endpoint not found"}, 404

if __name__ == "__main__":
    app.run(debug=True)
