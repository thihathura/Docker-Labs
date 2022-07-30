import os
from flask import Flask
app = Flask(__name__)

@app.route("/")
def main():
    return "Welcome to Y-Technologies!"

@app.route('/Welcome to Y-Technologies')
def hello():
    return 'Start Your Career with us'

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)