#!/usr/bin/python3
"""
A Flask script that start a web application
Listen on 0.0.0.0, port 5000
Routes:
    / => displays "Hello HBNB
"""

from flask import Flask


app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_route():
    """ Return a string route """
    return "Hello HBNB"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)