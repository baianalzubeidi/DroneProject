from utlis import *
import cv2
import time
import sys
import pynput
import keyboard

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

#missionOne(myDrone)

while True:
    currenttime = time.time()
    

    if (startCounter ==0 and currenttime - timer > 10):
        myDrone.takeoff()
        timer = time.time() 
        startCounter +=1

    if (startCounter ==1 and currenttime - timer > 10):
        myDrone.move_forward(150)
        timer = time.time()
        startCounter +=1
            
    if (startCounter ==2 and currenttime - timer > 10):
        myDrone.rotate_counter_clockwise(90)
        startCounter +=1
        timer = time.time()

    if (startCounter ==3 and currenttime - timer > 10):
        myDrone.move_forward(20)
        timer = time.time()
        startCounter +=1

    if (startCounter ==4 and currenttime - timer > 10):
        save = True
        startCounter +=1    
        timer = time.time()
    
    if (startCounter ==5 and currenttime - timer > 10):
        myDrone.move_back(20)
        startCounter +=1
        timer = time.time()
    
    #if (startCounter ==6 and currenttime - timer > 10):
        #myDrone.rotate_counter_clockwise(90)
        #startCounter +=1
        #timer = time.time()
    
    #if (startCounter ==7 and currenttime - timer > 10):
        #myDrone.move_forward(150)
        #timer = time.time()
        #startCounter +=1
    
    #if (startCounter ==8 and currenttime - timer > 10):
        #myDrone.land()
        #startCounter +=1
        #timer = time.time()

    #if (startCounter ==9 and currenttime - timer > 10):
        #break


    img = telloGetFrame(myDrone,w ,h)
    img, info = findFace(img)
    cv2.imshow("image",img)
    


    #if cv2.waitKey(1) & 0xFF == ord("s"):
        #save = True

    if (save == True and info[0][0] != 0 ):
        saveImage(info, img)
        save = False

    #if cv2.waitKey(1) & 0xFF == ord("q"):
        #myDrone.land()
    
    if keyboard.is_pressed('w'):
        print("forward")
        myDrone.move_forward()

    if keyboard.is_pressed('q'):
        print("land drone")
        myDrone.land()


cv2.destroyAllWindows()
myDrone.streamoff()