#!/usr/bin/env python3
import time
# from flask import Flask, render_template, Response
from camera import VideoCamera
import numpy as np
import cv2
import rospy
from std_msgs.msg import String, Float32
from playsound import playsound

DEBUG = False

global pubBase
pubBase = rospy.Publisher("base", String, queue_size=16)

# app = Flask(__name__)
# @app.route('/')
# def index():
#     return render_template('index.html')

def set_hsv():
    global USLOVNAYA_PEREMENNAYA,hsv_min, hsv_max
    if(USLOVNAYA_PEREMENNAYA == 0): # red
        hsv_min = np.array((0,42,125), np.uint8)
        hsv_max = np.array((12,137,194), np.uint8)
    elif USLOVNAYA_PEREMENNAYA == 1: # blu
        hsv_min = np.array((86,58,137), np.uint8)
        hsv_max = np.array((121,255,178), np.uint8)
    elif USLOVNAYA_PEREMENNAYA == 2: # green
        hsv_min = np.array((39,49,70), np.uint8)
        hsv_max = np.array((60,155,243), np.uint8)
    return

def color_check():
    global USLOVNAYA_PEREMENNAYA
    if USLOVNAYA_PEREMENNAYA == 2:
        USLOVNAYA_PEREMENNAYA = 0
        set_hsv()
        plstr = "/home/ubuntu/Project-WALLE/catkin_ws/src/walle/scripts/sounds/robo-short-47.wav"
        playsound(plstr)
        time.sleep(2)
        return
    if USLOVNAYA_PEREMENNAYA == 0:
        USLOVNAYA_PEREMENNAYA = 1
        set_hsv()
        plstr = "/home/ubuntu/Project-WALLE/catkin_ws/src/walle/scripts/sounds/robo-short-53.wav"
        playsound(plstr)
        time.sleep(2)
        return 
    if USLOVNAYA_PEREMENNAYA == 1:
        plstr = "/home/ubuntu/Project-WALLE/catkin_ws/src/walle/scripts/sounds/robo-long-15.wav"
        playsound(plstr)
        exit()
        return

def init_cv():
    global height, width, width_center, RECTCOLOR, RTHICK, hsv_min, hsv_max, kernel, BLOBSIZE_STOP, BLOBSIZE
    global my_color, crange
    height = 720
    width = 1280
    width_center=width/2;
    global USLOVNAYA_PEREMENNAYA
    USLOVNAYA_PEREMENNAYA = 2
    set_hsv()

    RECTCOLOR = (103, 143, 134)
    RTHICK = 2
    
    
    
    

    BLOBSIZE_STOP = 300000
    BLOBSIZE = 700
    my_color = (0,0,255)
    crange = [0,0,0, 0,0,0]

# if DEBUG:
    

# greeen
# hsv_min = np.array((51,49,47), np.uint8)
# hsv_max = np.array((84,255,255), np.uint8)

# red
# hsv_min = np.array((169,97,35), np.uint8)
# hsv_max = np.array((255,255,255), np.uint8)


# blue
# hsv_min = np.array((90,134,65), np.uint8)
# hsv_max = np.array((120,209,255), np.uint8)


def rotate_command(direction, amount = 0):
    delay = amount/640
    delay = 0.1
    if direction == "L":
        pubBase.publish("110"+" "+"60")
        time.sleep(delay)
        pubBase.publish("0"+" "+"0")
        
        
    elif direction == "R":
        pubBase.publish("70"+" "+"60")
        time.sleep(delay)
        pubBase.publish("0"+" "+"0")
        
        
    elif direction == "F":
        pubBase.publish("77"+" "+"60")
        time.sleep(1)
        pubBase.publish("0"+" "+"0")
    #time.sleep(1)
    return




def checkSize(w, h):
    if w * h > BLOBSIZE:
        return True
    else:
        return False
            
def stop(w,h):
    if w*h>BLOBSIZE_STOP:
        return True
    else:
        return False

def gen(camera):
    center_rectangle = 2
    x,y,w,h = 1,2,3,4
    #print("I M IN FUNC")
    while True:
        img = camera.get_frame()
        time.sleep(1)
        img = camera.get_frame()
        hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV )
        thresh = cv2.inRange(hsv, hsv_min, hsv_max )
        contours, hierarchy = cv2.findContours(thresh.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        kernel = np.ones((5, 5), np.uint8)
        cv2.dilate(thresh, kernel, iterations = 1)
        cv2.erode(thresh, kernel, iterations = 1)
        cv2.drawContours(img, contours, -1, (255, 0, 0), 2, cv2.LINE_AA, hierarchy, 0)
        cv2.drawContours(img, contours, -1, (255, 0, 0), 2, cv2.LINE_AA, hierarchy, 2)
        
        if len(contours) == 0:
            rotate_command("L", abs(width_center - center_rectangle))
            print("IA NI4EGO NE VIJU")
            print("!              ", end="")
        else:
            c = max(contours, key = cv2.contourArea)
            x,y,w,h = cv2.boundingRect(c)
        

        cv2.rectangle(img, (x, y), (x+w, y+h), RECTCOLOR, RTHICK)
        cv2.putText(img, str(x)+" "+str(y), (x,y), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, my_color, 2, cv2.LINE_AA)
        cv2.putText(img, str(x+h)+" "+str(y), (x+h,y), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, my_color, 2, cv2.LINE_AA)
        cv2.putText(img, str(x)+" "+str(y+w), (x,y+w), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, my_color, 2, cv2.LINE_AA)
        cv2.putText(img, str(x+h)+" "+str(y+w), (x+h,y+w), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, my_color, 2, cv2.LINE_AA)
        center_rectangle = x + h/2;


        if len(contours) != 0:
            
            
            if checkSize(w, h):
                # выводим его str("UP left")str("UP right")str("down left")str("down right")
                
                if stop(w,h):
                    print("usl"+str(USLOVNAYA_PEREMENNAYA))
                    print("\nSTOP")
                    # plstr = "/home/ubuntu/Project-WALLE/catkin_ws/src/walle/scripts/sounds/robo-short-47.wav"
                    # playsound(plstr)
                    
                    color_check()
                    print("usl"+str(USLOVNAYA_PEREMENNAYA))
                    continue
                elif (width_center < center_rectangle and abs(width_center-center_rectangle)>width_center/12):
                    print(" GO RIGHT", end="")
                    if not DEBUG:
                        rotate_command("R", abs(width_center - center_rectangle))
                        continue
                elif(width_center > center_rectangle and abs(width_center-center_rectangle)>width_center/12):
                    print(" GO LEFT", end="")
                    if not DEBUG:
                        rotate_command("L", abs(width_center - center_rectangle))
                        continue
                else: 
                    print("  GO FORWARD", end="")
                    if not DEBUG:
                        rotate_command("F", abs(width_center - center_rectangle))
                        continue

  
        rotate_command("L", abs(width_center - center_rectangle))
        print("IA NI4EGO NE VIJU")
        print("!              ", end="")


        time.sleep(1)
        # ret, jpeg = cv2.imencode('.jpg', img)
        # yield (b'--frame\r\n'
        #     b'Content-Type: image/jpeg\r\n\r\n' + jpeg.tobytes() + b'\r\n\r\n')




# @app.route('/video_feed')
# def video_feed():
#     return Response(gen(VideoCamera()),
#                     mimetype='multipart/x-mixed-replace; boundary=frame')


if __name__ == '__main__':
    rospy.init_node("cv_camera")
    # time.sleep(5)
    init_cv()
    time.sleep(11)
    plstr = "/home/ubuntu/Project-WALLE/catkin_ws/src/walle/scripts/sounds/robo-short-72.wav"
    playsound(plstr)
    gen(VideoCamera())

    # app.run(host='0.0.0.0', debug=True)