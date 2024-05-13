from flask import Flask

server = Flask(__name__)

@server.route('/')
def homepage():
    return"This is Home Page"

@server.route('/welcome')
def welcome():
    return"Welcome to Iot Application"

server.run(host='0.0.0.0')        