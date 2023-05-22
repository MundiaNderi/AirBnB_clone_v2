#!usr/bin/python3
"""
script that starts a Flask web application:
Your web application must be listening on 0.0.0.0, port 5000
Routes: 1- /: display “Hello HBNB!”
2- /hbnb: display “HBNB”
3- /c/<text>: display “C ” followed by the value of the text
variable (replace underscore _ symbols with a space )
4- /python/(<text>): display “Python ”, followed by the value of...
the text variable (replace underscore _ symbols with a space )
The default value of text is “is cool”
5- /number/<n>: display “n is a number” only if n is an integer
You must use the option strict_slashes=False in your route definition
"""
from flask import Flask
app = Flask(__name__)
app.url_map.strict_slashes = False
ip = '0.0.0.0'
port = 5000


@app.route('/')
def hello_hbnb():
    # says Hello HBNB when curl'd
    return ("Hello HBNB!")


@app.route('/hbnb')
def hbnb():
    # displays HBNB
    return ("HBNB")


@app.route('/c/<text>')
def c_text(text):
    # returns user text with C in front
    return ("C {}".format(text.replace("_", " ")))


@app.route('/python')
@app.route('/python/<text>')
def python_text(text='is cool'):
    # returns user text with Python in front
    return ("Python {}".format(text.replace("_", " ")))


@app.route('/number/<int:n>')
def num(n):
    # returns an integer
    return ("{} is a number".format(n))


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
