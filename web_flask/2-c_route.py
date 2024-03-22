#!/usr/bin/python3
""" second task in Flask """
from flask import Flask


app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello():
    """ Hello function return Word to /"""
    return "Hello HBNB!"

@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """ Return a word to /hbnb"""
    return "HBNB"

@app.route("/c/<text>", strict_slashes=False)
def c_is(text):
    """function that take an argument to pass into html"""
    return "C {}".format(text.replace("_"," "))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
