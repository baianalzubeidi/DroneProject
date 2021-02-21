from utlis import *
import cv2
import time
import sys
from flask import Flask

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
    return 'Hello, World!'

@app.route('/takeoff')
def takeoff():
    myDrone.takeoff()
    return 'takeoff'

@app.route('/forward')
def forward():
    myDrone.move_forward(20)
    return 'forward'

@app.route('/backward')
def backward():
    myDrone.move_back(20)
    return 'backward'

@app.route('/left')
def left():
    myDrone.move_left(20)
    return 'left'

@app.route('/right')
def move_right():
        myDrone.move_right(20)
        return 'right'

@app.route('/up')
def move_up():
        myDrone.move_up(20)
        return 'up'

@app.route('/down')
def move_down():
        myDrone.move_down(20)
        return 'down'

@app.route('/cw')
def rotate_clockwise():
        myDrone.rotate_clockwise(90)
        return 'cw'
        
@app.route('/ccw')
def rotate_counter_clockwise():
        myDrone.rotate_counter_clockwise(90)
        return 'ccw'

@app.route('/land')
def land():
    myDrone.land()
    return 'land'