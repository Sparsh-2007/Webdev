from flask import Flask

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

if __name__ == "__main__":
    app.run(debug=True)
