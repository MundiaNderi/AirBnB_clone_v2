#!/usr/bin/python3
"""
script that starts a Flask web application:
Your web application must be listening on 0.0.0.0, port 5000
Routes: 1- /: display “Hello HBNB!”
2- /hbnb: display “HBNB”
3- /c/<text>: display “C ” followed by the value of the text
variable (replace underscore _ symbols with a space )
You must use the option strict_slashes=False in your route definition
"""
from flask import Flask
app = Flask(__name__)
app.url_map.striact_slashes = False
ip = '0.0.0.0'
port = 5000


@app.route('/')
def hello_hbnb():
    """Route handler function for the root URL.
    Returns the string "Hello HBNB!" when the root URL is accessed.
    """
    return ("Hello HBNB")


@app.route('/hbnb')
def hbnb():
    """Route handler function for the '/hbnb' URL.
    Returns the string "HBNB" when the '/hbnb' URL is accessed.
    """
    return ("HBNB")


@app.route('/c/<text>')
def c_text(text):
    """Route handler function for the '/c/<text>' URL.
    Returns the string "C " followed by the value of the `text` variable.
    Underscore (_) symbols in the `text` variable are replaced with spaces.
    """
    return ("C {}".format(text.replace("_", " ")))


# Start the Flask application if this script is executed directly
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
