from utlis import *
import sys

w,h = 360,240
#PID      Kp    Ki   Kd
pidYaw = [0.5,  0.5, 0]
pidFB  = [0.01, 0.5, 0]
pidUD  = [0.5,  0.5, 0]

pError = 0
startCounter = 0 # to takeoff 0 , for no flying
save = False

#-------------------------
myDrone = IntializeTello()
filename = 'savedImage.jpg'
directory = r"/Users/byoon/PycharmProjects/internship/venv/lib/python3.7/DroneProject/"

def screenshot():
    img = telloGetFrame(myDrone,w ,h)
    cv2.imwrite(directory + filename, img)