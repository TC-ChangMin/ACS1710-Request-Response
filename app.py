from flask import Flask
import random

app = Flask(__name__)

@app.route('/')
def homepage():
    """Shows a greeting to the user."""
    return 'Are you there, world? It\'s me, Ducky!'

@app.route('/animal/<users_animal>')
def favorite_animal(users_animal):
    """Display a message to the user that changes based on their favorite animal."""
    return f'Wow, {users_animal} is my favorite animal, too!'

@app.route('/dessert/<users_dessert>')
def favorite_dessert(users_dessert):
    """Display a message to the user that changes based on their favorite dessert."""
    return f"How'd you know I liked {users_dessert} too?"

@app.route('/madlibs/<adjective>/<noun>')
def madlibs(adjective, noun):
    """Display a message to the user that changes based on their favorite dessert."""
    return f"So you also saw a {adjective} {noun} run that way?"

@app.route('/multiply/<number1>/<number2>')
def mult(number1, number2):
    """Display a message to the user that changes based on their favorite dessert."""
    if number1.isdigit() and number2.isdigit():
        return f"{number1} times {number2} is {int(number1) * int(number2)}."
    else:
        return "Invalid inputs. Please try again by entering 2 numbers!"
    
@app.route('/sayntimes/<word>/<n>')
def sayntimes(word, n):
    """Display a message to the user that changes based on their favorite dessert."""
    if n.isdigit():
        return f"{word} " * int(n)
    else:
        return "Invalid input. Please try again by entering a word and a number!"
    
@app.route('/dicegame')
def dicegame():
    dice_rolls = random.randint(1, 6)
    if dice_rolls == 6:
        return f"You rolled a {dice_rolls}. You won!"
    else:
        return f"You rolled a {dice_rolls}. You lost!"

if __name__ == '__main__':
    app.run(debug=True)