#!/usr/bin/python3
"""file to initialize the module"""

from flask import Flask




def starting_point():
    app = Flask(__name__)
    return app
