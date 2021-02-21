from flask import Flask
from faceTrackingTello import *
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/takeoff')
def takeoff():
    #myDrone.takeoff()
    return 'takeoff'