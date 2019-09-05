from flask import Flask, request
from random import choice, sample
import requests

app = Flask(__name__)

# fortune = [
#     'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza',
#     'oh-so-not-meh', 'brilliant', 'ducky', 'coolio', 'incredible',
#     'wonderful', 'smashing', 'lovely', 'tenacious', 'Pythonic']


@app.route('/')
def index():
    """Show the homepage and ask the user's name."""
    return """
    <form action='/fortune'>
        <p>
            What is your name?
            <input type="text" name="name"/>
        </p>
        <p>
            <input type="checkbox" name="show_fortune"/>
            Show fortune
        </p>
        <p>
            How many fortunes?
            <select name="num_fortune">
                <option value="1">One</option>
                <option value="2">Two</option>
                <option value="3">Three</option>
            </select>
        </p>
        <button type="submit">Submit</button>
    </form>
    """


@app.route('/fortune')
def get_fortune():
    """Give the user a fortune"""
    fortunes = []
    for i in range(3):
        r = requests.get('http://yerkee.com/api/fortune',
                         headers={'Content-Type': 'application/json'})
        fortunes.append(r.json()['fortune'])

    name = request.args.get('name')
    num_fortune = int(request.args.get('num_fortune'))
    show_fortune = request.args.get('show_fortune')
    all_fortunes = '</br> '.join(sample(fortunes, num_fortune))

    fortunes = []
    r = requests.get('http://yerkee.com/api/fortune',
                     headers={'Content-Type': 'application/json'})
    horoscope_item = r.json()['fortune']

    if show_fortune:
        return f'Hello there, {name}! Hey there, here are the fortunes that you requested:</br>  {all_fortunes}!'
    else:
        return f'Hello there, {name}! Have a nice day!'


if __name__ == '__main__':
    app.run(debug=True)
