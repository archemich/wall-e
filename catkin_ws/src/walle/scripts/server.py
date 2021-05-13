import os
import socket
import errno
import time
import rospy
from std_msgs.msg import String, Float32
from socket import error as SocketError
from playsound import playsound

import RPi.GPIO as GPIO
from adafruit_servokit import ServoKit

global moveAngle
moveAngle = 0


def on_board_systems_check():
    #pubVoice.publish("play robo-short-64")
    plstr = "/home/ubuntu/Project-WALLE/catkin_ws/src/walle/scripts/sounds/robo-short-64.wav"
    playsound(plstr)

    mess = "L 90"
    for i in range(180):
        mess = 'L' + ' ' + str(i)
        pubServos.publish(mess)
        time.sleep(0.01)
    for i in range(180):
        mess = 'R' + ' ' + str(i)
        pubServos.publish(mess)
        time.sleep(0.01)   

def publisher_setup():
    global pubVoice
    pubVoice = rospy.Publisher("voice", String, queue_size=1)
    global pubBase
    pubBase = rospy.Publisher("base", String, queue_size=16)
    global pubServos
    pubServos = rospy.Publisher("joints", String, queue_size=16)
    pubDist = rospy.Publisher("distance", String, queue_size=50)

# Parsing the received command
def check_parse(messArr):
    global moveAngle
    
    parsedLine = messArr.split(" ")

    if parsedLine[0] == 'J':
        mess = ""
        mess += parsedLine[1] + " " +  parsedLine[2]
        # mess.append(int(parsedLine[2]))
        # mess.append(int(parsedLine[1]))
        # rospy.loginfo(mess)
        if (int(parsedLine[1]) > (moveAngle+5)) or (int(parsedLine[1]) < (moveAngle-5)) or (int(parsedLine[2]) == 0):
            pubBase.publish(mess)
            rospy.loginfo(" | ".join(parsedLine))
            if not(int(parsedLine[2]) == 0):
                pubVoice.publish("play robo-short-56")
        # rospy.loginfo("play robo-short-64")
        moveAngle = int(parsedLine[1])
        rate.sleep()
    elif parsedLine[0] == 'L' or parsedLine[0] == 'R':
        mess = ""
        mess += parsedLine[0] + " " + parsedLine[1]
        # rospy.loginfo(mess)
        pubServos.publish(mess)
        rate.sleep()
    elif parsedLine[0] == 'T':
        mess = ""
        mess += parsedLine[0] + " " + parsedLine[1] + " " + parsedLine[2]
        # rospy.loginfo(mess)
        pubServos.publish(mess)
        rate.sleep()
    if parsedLine[0] == 'E':
        return 1


def main():
    port = 2000

    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    ip = s.getsockname()[0]
    s.close()

    server = socket.socket(
        socket.AF_INET,
        socket.SOCK_STREAM,
    )

    server.bind((ip, port))
    print("Server started:",ip,',',port)
    
    server.listen()
    ret = 0
    while True:
        user_socket, address = server.accept()
        user_socket.send("Your connected".encode("utf-8"))
        messArr = []
        try:
            data = user_socket.recv(2048)
        except SocketError as e:
            if e.errno != errno.ECONNRESET:
                RAISE
            pass
        messArr = data.decode("utf-8")
        ret = check_parse(messArr)
        if ret == 1:
            exit(0)
        print(data.decode("utf-8"))


if __name__ == '__main__': 
    rospy.init_node('server')
    global rate
    rate = rospy.Rate(150)
    print("\nCalibration ... ",end='')

    publisher_setup()
    print("done !!!")
    on_board_systems_check()

    # Start listening
    main()  