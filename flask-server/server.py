from flask import Flask
from flask_cors import CORS
from main import convert_to_vai, convert_to_cherokee

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

@app.route('/hello')
def hello():
    return 'Hello, World!'

@app.route('/vai/<text>')
def vai(text):
    vai_text = convert_to_vai(text)
    return vai_text

@app.route('/cherokee/<text>')
def cherokee(text):
    print("Received text for Cherokee conversion:", text)
    cherokee_text = convert_to_cherokee(text)
    print("Converted Cherokee text:", cherokee_text)
    return cherokee_text

if __name__ == '__main__':
    app.run(debug=True)