#!/usr/bin/python3
"""
starts a Flask web application
web application must be listening on 0.0.0.0, port 5000
"""
from models import storage
from models import *
from flask import Flask, render_template
app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/states_list')
def states_list():
    """display a HTML page with the list of all State objects present in
    DBStorage sorted by name"""
    states = storage.all("State")
    return render_template("7-states_list.html", states=states)


@app.teardown_appcontext
def tear_down(self):
    """remove the current SQLAlchemy Session"""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
