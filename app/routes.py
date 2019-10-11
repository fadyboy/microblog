from flask import render_template
from app import app

@app.route("/")
@app.route("/index")
def index():
    user = {"username": "Fady"}
    posts = [
        {"author": {"username": "Fady"},
         "body": "This is my first body"
         },
        {
          "author": {"username": "Miguel"},
          "body": "This is my second body"
        }
    ]
    return render_template("index.html", title="Home", user=user, posts=posts)
