import os

from flask import Flask, render_template, request
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

#engine used to manage connections to the database user environment variable
engine=create_engine(os.getenv("DATABASE_URL"))

#create scoped session so individuals operate on separate sessions
db=scoped_session(sessionmaker(bind=engine))

app=Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    return render_template("login.html")

@app.route("/login", methods=["POST"])
def login():
    username=request.form.get("username")
    password=request.form.get("password")

    #pseudocode check if username/password is in database if successful send them to success page
    #if username/password isn't in database redirect them to login.html and tell them to try again

    return render_template("success.html", username=username, password=password)
