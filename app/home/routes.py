from flask import Flask, render_template
from app.home import home


@home.route('/')
def start():
    return render_template('index.html')
