#!/usr/bin/python3
"""
starts a Flask web application
web application must be listening on 0.0.0.0, port 5000
"""
from models import storage
from models import *
from flask import Flask, render_template
app = Flask(__name__)


@app.route("/states", strict_slashes=False)
def states():
    """
    display a HTML page with the list of all State objects present
    in DBStorage sorted by name
    """
    states = storage.all("State")
    return render_template("9-states.html", state=states)


@app.route("/states/<id>", strict_slashes=False)
def states_id(id):
    """
    display a HTML page with the list of City objects
    linked to the State sorted by name
    """
    for state in storage.all("State").values():
        if state.id == id:
            return render_template("9-states.html", state=state)
    return render_template("9-states.html")


@app.teardown_appcontext
def teardown(exc):
    """Remove the current SQLAlchemy session."""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
