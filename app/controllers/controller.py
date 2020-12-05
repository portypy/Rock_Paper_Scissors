from flask import render_template, redirect, request 
from app import app
from app.modules.game import Game
from app.modules.player import Player
from app.modules import random_generator

import pdb

@app.route('/')
def index():
     return render_template('welcome.html', title='Home')

@app.route('/<choice1>/<choice2>')
def check(choice1,choice2):
    game = Game()
    result = game.game(choice1,choice2)
    return render_template('index.html', title='Home', choice1=choice1,choice2=choice2, result=result)
    
@app.route('/play', methods =['POST', 'GET'] )
def play():
     if request.method == 'POST':
          game = Game()
          random_str = random_generator.str_generator()
          result = game.game(request.form['choice7'],random_str)
          return render_template('results.html', result=result, random_str=random_str)
     else:
          return render_template("tempo.html")