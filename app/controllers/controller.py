from flask import render_template, redirect
from app import app
from app.modules.game import Game


@app.route('/')
def index():
     return render_template('index.html', title='Home')

@app.route('/<choice1>/<choice2>')
def check(choice1,choice2):
    game = Game()
    result = game.game(choice1,choice2)

    return render_template('index.html', title='Home', choice1=choice1,choice2=choice2, result=result)
    