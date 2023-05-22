#!/usr/bin/python3
# starts a Flask web app
from flask import Flask

# Create a Flask Web Application
app = Flask(__name__)

# Disable strict slashes at the end
app.url_map.strict_slashes = False

# Define the IP address and port of the server
ip = '0.0.0.0'
port = 5000


@app.route('/')
def hello_hbnb():
    """Route handler function for the root URL.
    Returns the string "Hello HBNB!" when the root URL is accessed.
    """
    return ("Hello HBNB!")


@app.route('/hbnb')
def hbnb():
    """
    Route handler function for the root URL.
    Returns the string "Hello HBNB!" when the root URL is accessed.
    """
    return ("HBNB")


# # Start the Flask application if this script is executed directly
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
