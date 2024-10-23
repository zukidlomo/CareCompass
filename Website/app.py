
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/index')
def index_page():
    return render_template('index.html')

@app.route('/login')
def login():
    return render_template('loginPage.html')

@app.route('/signup_page')
def signup_page():
    return render_template('signupPage.html')

@app.route('/sponsor')
def sponsor():
    return render_template('sponsor.html')

@app.route('/map')
def map():
    return render_template('map.html')

if __name__ == '__main__':
    app.run(debug=True, port=8000)

