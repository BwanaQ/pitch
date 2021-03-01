from flask import Flask, render_template
from app import app


@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Tom'}
    pitches = [
        {
            'author': 'Tom Hunja',
            'title': 'First Pitch',
            'category': 'Inspirational',
            'description': 'First pitch ever',
            'date_posted': 'Feb 27, 2021',
            'votes': 10
        },
        {
            'author': 'Breens Mbaka',
            'title': 'Second Pitch',
            'category': 'Dating',
            'description': 'First pitch ever',
            'date_posted': 'Feb 1, 2020',
            'votes': 40
        },
        {
            'author': 'James Hunja',
            'title': 'greatest joke',
            'category': 'Funny',
            'description': 'Haha',
            'date_posted': 'Feb 27, 2021',
            'votes': 0
        }
    ]
    return render_template('index.html', pitches=pitches, user=user)
