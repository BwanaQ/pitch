from flask import Flask, render_template
from app import app
from app.forms import LoginForm, RegistrationForm


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


@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', title='Sign In', form=form)


@app.route('/registration')
def registration():
    form = RegistrationForm()
    return render_template('registration.html', title='Sign Up', form=form)
