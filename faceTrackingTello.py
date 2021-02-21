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
    #myDrone.takeoff()
    return 'takeoff'