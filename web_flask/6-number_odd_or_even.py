#!/usr/bin/python3
"""
A Flask script that start a web application
Listen on 0.0.0.0, port 5000
Routes:
    / => displays "Hello HBNB
    /hbnb => "HBNB"
    /c/<text> => displays "C" followed by value of text
    /python/<text> => displays "Python" followed by value of texxt
    /number/<n> => displays "n" is a number oonly if n is an integer
    /number_template/<n> => display an HTML template if n is an integer
    /number_odd_or_even/<n> => displaya an HTML template if n is even|odd
"""

from flask import Flask
from flask import render_template


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

@app.route("/number/<int:n>", strict_slashes=False)
def number_route(n):
    """ Displays n with route """
    return "{} is a number".format(n)

@app.route("/number_template/<int:n>", strict_slashes=False)
def number_template(n):
    """ Displays a HTML page only if n is an integer """
    return render_template("5-number.html", n=n)

@app.route("/number_odd_or_even/<int:n>", strict_slashes=False)
def number_odd_or_even(n):
    """ Displays n if it is odd or even """
    return render_template("6-number_odd_or_even.html", n=n)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)