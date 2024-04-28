from flask import Flask, render_template, request
import random

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/play', methods=['POST'])
def play():
    user_choice = request.form['choice']
    choices = ['rock', 'paper', 'scissors']
    computer_choice = random.choice(choices)
    
    # Game logic
    # Rock beats scissors, scissors beats paper, paper beats rock
    if user_choice == computer_choice:
        result = 'It\'s a tie!'
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'scissors' and computer_choice == 'paper') or \
         (user_choice == 'paper' and computer_choice == 'rock'):
        result = 'You win!'
    else:
        result = 'Computer wins!'
    
    return render_template('result.html', user_choice=user_choice, computer_choice=computer_choice, result=result)

if __name__ == '__main__':
    app.run(debug=True)
