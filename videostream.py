from utlis import *
import cv2
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

while True:
    img = telloGetFrame(myDrone,w ,h)
    cv2.imshow("image",img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break