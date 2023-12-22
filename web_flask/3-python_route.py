#!/usr/bin/python3
"""
A Flask script that start a web application
Listen on 0.0.0.0, port 5000
Routes:
    / => displays "Hello HBNB
    /hbnb => "HBNB"
    /c/<text> => displays "C" followed by value of text
    /python/<text> => displays "Python" followed by value of texxt
"""

from flask import Flask


app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_route():
    """ Return a string route """
    return "Hello HBNB"

@app.route("/hbnb", strict_slashes=False)
def hbnb_route():
    """ Displays HBNB on route """
    return "HBNB"

@app.route("c/<text>", strict_slahses=False)
def c_route(text):
    """ Display of <text> with route """
    text = text.replace("_", " ")
    return "c {}".format(text)

@app.route("/pytohn", strict_slashes=False)
@app.route("/python/<string:text>", strict_slashes=False)
def python_route(text="is cool"):
    """ Displays value of <text with route """
    text = text.replace("_", " ")
    return "Python {}".format(text)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)