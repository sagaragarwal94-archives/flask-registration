from flask import render_template
from app.home import home


@home.route('/')
def start():
    return render_template('index.html')


@home.route('/sign')
def sign():
    return render_template('home/sign.html')


@home.route('/register')
def register():
    return render_template('home/register.html')