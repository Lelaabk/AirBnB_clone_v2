#!/usr/bin/python3
""" Starts Flask web application """

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """ Displays 'Hello HBNB!' """
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def display_hbnb():
    """ Display 'HBNB' """
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def display_c_text(text):
    """ Display 'C' followed by value of text variable """
    return 'C {}'.format(text.replace('_', ' '))


@app.route('/python/<text>', strict_slashes=False)
@app.route('/python', strict_slashes=False)
def display_python_text(text="is cool"):
    """ Display 'Python' followed by value of text variable """
    return 'Python {}'.format(text.replace('_', ' '))


@app.route('/number/<int:n>', strict_slashes=False)
def is_number(n):
    """ Display 'n is number' only if n is integer """
    return '{} is a number'.format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """ Display HTML page only if n is int """
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def number_odd_or_even(n):
    """ Display HTML page only if n is int, indicating it's odd or even """
    return render_template('6-number_odd_or_even.html', n=n,
                           even_or_odd=('even' if n % 2 == 0 else 'odd'))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
