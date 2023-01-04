from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("login.html")
    else:
        return "you are trying to log in"

@app.route("register", methods=["GET", "POST"])
def register():
    if request.method == "GET":
        return "this is the register page"
    else:
        return "trying to register"

@app.route("/home")
def home():
    return render_template("home.html")

@app.route("/messages")
def messages():
    return "here are your messages"

@app.route("/profile/<trainer_id>")
def profile(trainer_id):
    return f"this is the profile of trainer {trainer_id}"

if __name__ == "__main__":
    app.run(debug=True)