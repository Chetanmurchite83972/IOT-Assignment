from flask import Flask

server = Flask(__name__)

@server.route('/')
def root():
    return "This is my First Flask server"

server.run()    