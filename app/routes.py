from . import app

from flask import render_template

@app.route('/')
def homePage():
    return render_template('index.html')
