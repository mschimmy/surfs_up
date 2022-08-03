#9.4.3 import Flask dependencies
from flask import Flask

# create a new flask app insance
app = Flask(__name__)

# create starting point for route
@app.route('/')
def hello_world():
    return 'Hello world'
