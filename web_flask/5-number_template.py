#!/usr/bin/python3
"""This module starts a Flask web app.
Your web application must be listening on 0.0.0.0, port 5000
Routes: 1- /: display “Hello HBNB!”
2- /hbnb: display “HBNB”
3- /c/<text>: display “C ” followed by the value of the text
variable (replace underscore _ symbols with a space )
4- /python/(<text>): display “Python ”, followed by the value of...
the text variable (replace underscore _ symbols with a space )
The default value of text is “is cool”
5- /number/<n>: display “n is a number” only if n is an integer
6- /number_template/<n>: display a HTML page only if n is an...
...integer: H1 tag: “Number: n” inside the tag BODY
You must use the option strict_slashes=False in your route definition
"""

from flask import Flask, render_template

app = Flask(__name__)
app.url_map.strict_slashes = False
ip = '0.0.0.0'
port = 5000


@app.route('/')
def hello_hbnb():
    """Displays 'Hello HBNB' when curl'd."""
    return "Hello HBNB!"


@app.route('/hbnb')
def hbnb():
    """Displays 'HBNB'."""
    return "HBNB"


@app.route('/c/<text>')
def c_text(text):
    """Returns user text with 'C' in front."""
    return "C {}".format(text.replace("_", " "))


@app.route('/python')
@app.route('/python/<text>')
def python_text(text='is cool'):
    """Returns user text with 'Python' in front."""
    return "Python {}".format(text.replace("_", " "))


@app.route('/number/<int:n>')
def num(n):
    """Returns a message indicating that the input is a number."""
    return "{} is a number".format(n)


@app.route('/number_template/<int:n>')
def num_template(n):
    """Renders an HTML template if n is an integer."""
    return render_template('5-number.html', n=n)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
