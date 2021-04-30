#!/usr/bin/env python3
from flask import Flask, render_template, Response
from camera import VideoCamera
import numpy as np
import cv2
import rospy

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

def gen(camera):
    while True:
        USLOVNAYA_PEREMENNAYA = 0
        RECTCOLOR = (0, 255, 0)
        RTHICK = 2
        if(USLOVNAYA_PEREMENNAYA == 0):
            hsv_min = np.array((40,100,100), np.uint8)
            hsv_max = np.array((80,255,255), np.uint8)
        else:
            hsv_min = np.array((110,120,120), np.uint8)
            hsv_max = np.array((130,255,255), np.uint8)
        
        BLOBSIZE_STOP = 40000
        BLOBSIZE = 700
        my_color = (0,0,255)
        crange = [0,0,0, 0,0,0]
        
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

        height = 720
        width = 1280
        width_center=width/2;
        img = camera.get_frame()
        hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV )
        thresh = cv2.inRange(hsv, hsv_min, hsv_max )
        contours, hierarchy = cv2.findContours(thresh.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        kernel = np.ones((5, 5), np.uint8)
        cv2.dilate(thresh, kernel, iterations = 1)
        cv2.erode(thresh, kernel, iterations = 1)
        cv2.drawContours(img, contours, -1, (255, 0, 0), 2, cv2.LINE_AA, hierarchy, 0)
        cv2.drawContours(img, contours, -1, (255, 0, 0), 2, cv2.LINE_AA, hierarchy, 2)
        center_rectangle = 2
        x,y,w,h = 1,2,3,4
        if len(contours) != 0:
            c = max(contours, key = cv2.contourArea)
            x,y,w,h = cv2.boundingRect(c)
            if checkSize(w, h):
                # выводим его str("UP left")str("UP right")str("down left")str("down right")
                cv2.rectangle(img, (x, y), (x+w, y+h), RECTCOLOR, RTHICK)
                cv2.putText(img, str(x)+" "+str(y), (x,y), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, my_color, 2, cv2.LINE_AA)
                cv2.putText(img, str(x+h)+" "+str(y), (x+h,y), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, my_color, 2, cv2.LINE_AA)
                cv2.putText(img, str(x)+" "+str(y+w), (x,y+w), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, my_color, 2, cv2.LINE_AA)
                cv2.putText(img, str(x+h)+" "+str(y+w), (x+h,y+w), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, my_color, 2, cv2.LINE_AA)
                center_rectangle = x + h/2;
                if stop(w,h):
                    print("STOP")
                else: 
                    if(width_center < center_rectangle and abs(width_center-center_rectangle)>width_center/2):
                        print("GO RIGHT")
                    else: 
                        if(width_center > center_rectangle and abs(width_center-center_rectangle)>width_center/2):
                            print("GO LEFT")
                        else: 
                            print("GO FORWARD")
            
        
        ret, jpeg = cv2.imencode('.jpg', img)
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + jpeg.tobytes() + b'\r\n\r\n')

@app.route('/video_feed')
def video_feed():
    return Response(gen(VideoCamera()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    rospy.init_node("cv_camera")
    app.run(host='0.0.0.0', debug=True)
