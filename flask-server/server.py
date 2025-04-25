from flask import Flask
from main import convert_to_vai, convert_to_cherokee

app = Flask(__name__)

@app.route('/hello')
def hello():
    return 'Hello, World!'

@app.route('/vai/<text>')
def vai(text):
    vai_text = convert_to_vai(text)
    return vai_text

@app.route('/cherokee/<text>')
def cherokee(text):
    cherokee_text = convert_to_cherokee(text)
    return cherokee_text


if __name__ == '__main__':
    app.run()