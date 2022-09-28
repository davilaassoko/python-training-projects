from flask import Flask

from random import randint

app = Flask(__name__)

my_random_number = randint(0, 10)

@app.route('/<int:guest_number>')
def guest_number(guest_number):
    rps = ''
    if guest_number < my_random_number:
        rps = f'<h1 style="color: red">{my_random_number} Too low, try again!</h1>' \
              f'<img src="https://media2.giphy.com/media/12G1D7rPEV5Cfu/giphy.gif?cid=790b7611d9f14b32a5d0a3386ba4c799d82cb36cbc63f2d8&rid=giphy.gif&ct=g" width="300">'
    elif guest_number > my_random_number:
        rps = f'<h1 style="color: red">{my_random_number} Too high, try again!</h1>'\
              f'<img src="https://media4.giphy.com/media/1irfi6MmcGGc751W16/giphy.gif?cid=790b7611c94cc61fd4e9550566545f8d6bb952c1aa976f3b&rid=giphy.gif&ct=g" width="300">'
    else:
        rps = f'<h1 style="color: green">You found me!</h1>' \
              f'<img src="https://media0.giphy.com/media/LwFBZ6bUq3trKRphqq/giphy.gif?cid=790b761125b729b702c72aa38da4f8a2d24176143a6d80f7&rid=giphy.gif&ct=g" width="300">'


    return rps

@app.route('/')
def home():
    return '<h1>Guess a number between 0 and 9</h1>' \
           '<img src="https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif">'
