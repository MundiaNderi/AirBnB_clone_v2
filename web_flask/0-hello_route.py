#!/usr/bin/python3
"""write a script that starts a Flask web application:
    Your web application must be listening on 0.0.0.0, port 5000
    Routes: /: display “Hello HBNB!”
    You must use the option strict_slashes=False in your route definition
"""
from flask import Flask

# Create a Flask web application
app = Flask(__name__)

# Disable strict slashes at the end
app.url_map.strict_slashes = False

# Define the IP address and port for the server
ip = '0.0.0.0'
port = 5000


# Define a route for the root URL
@app.route('/airbnb-onepage/')
def hello_hbnb():
    # returns Hello HBNB when curl'd
    return ("Hello HBNB!")


# Start the Flask application if this script is executed directly
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
