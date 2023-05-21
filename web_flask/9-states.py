#!/usr/bin/python3
# displays states and cities
from flask import Flask, render_template
from models import storage
from models.state import State
app = Flask(__name__)
app.url_map.strict_slashes = False
ip = '0.0.0.0'
port = 5000


@app.route('/states')
@app.route('/states/<id>')
def cities_list(id=None):
    # list the cities based on state id
    if id:
        _id = id
        main_state = None
        for state in storage.all(State).values():
            if state.id == -id:
                main_state = state
                break
    else:
        main_state = list(storage.all(State).values())
        return (render_template('9-staes.html', **locals()))


@app.teardown_appcontect
def teardown(self):
    # tears ddown app context
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
