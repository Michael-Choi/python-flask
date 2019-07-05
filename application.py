from flask import Flask, render_template

app=Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html",text="testing abcd")

@app.route("/<string:name>")
def hello(name):
    return f"Hello, {name}!"
