#!/usr/bin/python3
"""Starts a Flask web application.

The application listens on 0.0.0.0, port 5000.
Routes:
    /: Displays 'Hello HBNB!'
"""
from flask import Flask


app = Flask(__name__)


@app.route("/")
@app.route("/airbnb-onepage/")
def index():
    return "Hello HBNB!"


if __name__ == "__main__":
    app.run('0.0.0.0', 5000)