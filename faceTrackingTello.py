from utlis import *
import cv2
import time
import sys
from flask import Flask
from flask import render_template

app = Flask(__name__)

w,h = 360,240
#PID      Kp    Ki   Kd
pidYaw = [0.5,  0.5, 0]
pidFB  = [0.01, 0.5, 0]
pidUD  = [0.5,  0.5, 0]

pError = 0
startCounter = 0 # to takeoff 0 , for no flying
save = False
timer = time.time()

#-------------------------
myDrone = IntializeTello()

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