from utlis import *
import cv2
import time

w,h = 320,240
#PID      Kp    Ki   Kd
pidYaw = [0.5,  0.5, 0]
pidFB  = [0.01, 0.5, 0]
pidUD  = [0.5,  0.5, 0]

pError = 0
startCounter = 1 # to takeoff 0 , for no flying
save = False

#-------------------------
myDrone = IntializeTello()

#missionOne(myDrone)

while True:
    currenttime = time.time()
    timer = time.time()

    if startCounter ==0:
        myDrone.takeoff()
        startCounter +=1

    if (startCounter ==1 and currenttime - timer > 10):
        myDrone.move_forward(100)
        startCounter +=1
            
    #if (startCounter ==2 and time.time()-timer > 10)
        #myDrone.rotate_counter_clockwise(90)
        #startCounter +=1
        #timer = time.time()

    if (startCounter ==3 and currenttime - timer > 10):
        save = True
        startCounter +=1    



    img = telloGetFrame(myDrone,w ,h)
    img, info = findFace(img)
    cv2.imshow("image",img)
    if (info[0][0]!=0):
        saveImage(info,img)
        cv2.destroyAllWindows()
        myDrone.streamoff()
        break

#missionTwo(myDrone)

#if cv2.waitKey(1) & 0xFF == ord("s"):
    #save = True

if (save == True and info[0][0] != 0 ):
    saveImage(info, img)
    save = False

#if cv2.waitKey(1) & 0xFF == ord("q"):
    #myDrone.land()






