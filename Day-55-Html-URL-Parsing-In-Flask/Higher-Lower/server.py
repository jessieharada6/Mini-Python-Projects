from flask import Flask
import random

# def h1(function):
#     def wrapper():
#         return f'<h1>{function()}</h1>'
#     return wrapper

#global so it is consistent in one game
random_number = random.randint(0, 9)

app = Flask(__name__)

@app.route("/")
def home_page():
    return "<h1>Guess a number between 0 and 9</h1>"\
           '<img src="https://media.giphy.com/media/dsLRESPtvjHdO5odzM/giphy.gif">'

@app.route("/guess/<int:number>")
def guess_the_number(number):
    print(random_number)
    if number == random_number:
        return \
            '<h1>You found me</h1>'\
            '<img src="https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif">'
    elif number < random_number:
        return \
            '<h1>Too Low</h1>' \
            '<img src="https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif">'
    else:
        return \
            '<h1>Too High</h1>' \
            '<img src="https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif">'

if __name__ == "__main__":
    app.run(debug = True)