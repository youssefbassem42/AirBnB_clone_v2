#!/usr/bin/python3
""" state list task """
from flask import Flask, render_template
from models.state import State
from models import storage


app = Flask(__name__)


app.route("/states_list", strict_slashes=False)
def state_list():
    """ function to list items from database in html elements"""
    states = storage.all()
    return render_template("7-states_list.html", states=states)


@app.teardown_appcontext
def teardown(self):
    """ function to close the sqlalchemy session"""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
