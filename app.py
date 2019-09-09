from flask import Flask, request, render_template
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
    return render_template('index.html')


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
    all_fortunes = sample(fortunes, num_fortune)

    fortunes = []
    r = requests.get('http://yerkee.com/api/fortune',
                     headers={'Content-Type': 'application/json'})
    horoscope_item = r.json()['fortune']

    return render_template('fortune.html', name=name, show_fortune=show_fortune,  all_fortunes=all_fortunes)


if __name__ == '__main__':
    app.run(debug=True)
