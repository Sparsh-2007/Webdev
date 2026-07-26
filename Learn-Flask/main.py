from flask import Flask, render_template

app = Flask(__name__)

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
    # test integer parameter
    return {"user_id": id, "type": "integer"}

if __name__ == "__main__":
    app.run(debug=True)
