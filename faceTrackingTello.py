from utlis import *
import time
import sys
from flask import Flask
from flask import render_template, send_file
from videostream import *

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('TelloDrone.html')

@app.route('/takeoff')
def takeoff():
    myDrone.takeoff()
    return render_template('TelloDrone.html')

@app.route('/forward')
def forward():
    myDrone.move_forward(20)
    return render_template('TelloDrone.html')

@app.route('/backward')
def backward():
    myDrone.move_back(20)
    return render_template('TelloDrone.html')

@app.route('/left')
def left():
    myDrone.move_left(20)
    return render_template('TelloDrone.html')

@app.route('/right')
def move_right():
    myDrone.move_right(20)
    return render_template('TelloDrone.html')

@app.route('/up')
def move_up():
    myDrone.move_up(20)
    return render_template('TelloDrone.html')

@app.route('/down')
def move_down():
    myDrone.move_down(20)
    return render_template('TelloDrone.html')

@app.route('/cw')
def rotate_clockwise():
    myDrone.rotate_clockwise(90)
    return render_template('TelloDrone.html')
        
@app.route('/ccw')
def rotate_counter_clockwise():
    myDrone.rotate_counter_clockwise(90)
    return render_template('TelloDrone.html')

@app.route('/land')
def land():
    myDrone.land()
    return render_template('TelloDrone.html')

@app.route('/picture')
def picture():
    screenshot()
    return send_file(directory + filename, mimetype='image/jpeg')