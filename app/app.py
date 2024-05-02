from flask import Flask, render_template
import random

app = Flask(__name__)

# Landing page
@app.route('/')
def index():
    return render_template('index.html')

# Coin toss route
@app.route('/toss_coin')
def toss_coin():
    result = random.choice(['Heads', 'Tails'])
    return render_template('result.html', result=result)

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=8080)

