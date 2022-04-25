# Create a new python file
from flask import Flask

# Create a new flask App instance
app = Flask(__name__)

# Flask route
@app.route('/')
def hello_world():
    return 'Hello world'