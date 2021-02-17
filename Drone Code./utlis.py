from djitellopy import Tello
import cv2
import numpy as np
import os
import time

directory = r"/Users/byoon/PycharmProjects/internship/venv/lib/python3.7/site-packages/DroneProject/face "
imgDirectory = r"/Users/byoon/PycharmProjects/internship/venv/lib/python3.7/site-packages/DroneProject"

def IntializeTello():
    myDrone = Tello()
    myDrone.connect()
    myDrone.for_back_velocity = 0
    myDrone.left_right_velocity = 0
    myDrone.up_down_velocity = 0
    myDrone.yaw_velocity= 0
    myDrone.speed = 0
    print(myDrone.get_battery())
    myDrone.streamoff()
    myDrone.streamon()
    return myDrone

def telloGetFrame(myDrone, w=360, h=240):
    myFrame = myDrone.get_frame_read()
    myFrame = myFrame.frame
    img = cv2.resize(myFrame,(w,h))
    return img

def findFace(img):
    faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(imgGray, 1.3, 5)

    myFaceListC = []
    myFaceListArea = []


    for (x,y,w,h)in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)
        cx = x + w//2
        cy = y + h//2
        area = w*h
        myFaceListArea.append(area)
        myFaceListC.append([cx,cy])
    if len(myFaceListArea)!=0:
        i = myFaceListArea.index(max(myFaceListArea))
        return img, [myFaceListC[i],myFaceListArea[i]]
    else:
        return img, [[0,0],0]

def saveImage(info, img):
    if info[0][0] != 0:
        os.chdir(imgDirectory)
        filename = "face.jpg"
        cv2.imwrite(filename,img)
        os.chdir(directory)
    return

def trackFace(myDrone, info, w, h, pidYaw, pidFB, pidUD, pError):
    
    #print(speed)
    if info[0][0] !=0:
        ##PID
        error = info[0][0]-w//2
        speed = pidYaw[0]*error + pidYaw[1]*(error-pError)
        speed = int(np.clip(speed, -100, 100))
        myDrone.yaw_velocity = speed

        errorUD = info[0][1]-h//2
        speedUD = pidUD[0]*errorUD *-1
        speedUD = int(np.clip(speedUD, -100, 100))
        myDrone.up_down_velocity = speedUD

        errorFB = 5000 - info[1]
        speedFB = pidFB[0]*errorFB
        speedFB = int(np.clip(speedFB, -50, 50))
        myDrone.for_back_velocity = speedFB
        
    else:
        myDrone.for_back_velocity = 0
        myDrone.left_right_velocity = 0
        myDrone.up_down_velocity = 0
        myDrone.yaw_velocity = 0
        error= 0

    if myDrone.send_rc_control:
        myDrone.send_rc_control(myDrone.left_right_velocity, myDrone.for_back_velocity,myDrone.up_down_velocity, myDrone.yaw_velocity)
    
    return error

def missionOne (myDrone):
    myDrone.takeoff()
    myDrone.move_forward(50)
    myDrone.rotate_clockwise(90)
    myDrone.move_forward(20)
    return

def faceDetect (img, info):
    while True:
        img = telloGetFrame(myDrone,w,h)
        img, info = findFace(img)
    
        cv2.imshow("Image",img)

        if (info[0][0] != 0 ):
            saveImage(info, img)
            break
    return 


def missionTwo (myDrone):
    myDrone.move_back(50)
    myDrone.rotate_clockwise(90)
    myDrone.move_forward(50)
    myDrone.land()
    return