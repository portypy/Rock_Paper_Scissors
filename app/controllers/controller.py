from flask import render_template
from app import app
from app.modules import player


@app.route('/')
def inedx():
    return render_template('index.html', title='Home')