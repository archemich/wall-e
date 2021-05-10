import os
import socket
import errno
import time
import rospy
from std_msgs.msg import String
from socket import error as SocketError

import RPi.GPIO as GPIO
from adafruit_servokit import ServoKit

def publisher_setup():
    global pubVoice
    pubVoice = rospy.Publisher("voice", String, queue_size=16)
    global pubBase
    pubBase = rospy.Publisher("base", String, queue_size=16)
    global pubServos
    pubServos = rospy.Publisher("joints", String, queue_size=16)
    pubDist = rospy.Publisher("distance", String, queue_size=50)


# Parsing the received command
def check_parse(messArr):
    rospy.loginfo(messArr)
    parsedLine = messArr.split(" ")
    print(" \ ".join(parsedLine))
    if parsedLine[0] == 'J':
        mess = ""
        mess += parsedLine[1] + " " +  parsedLine[2]
        # mess.append(int(parsedLine[2]))
        # mess.append(int(parsedLine[1]))
        # rospy.loginfo(mess)
        pubBase.publish(mess)
        pubVoice.publish("play robo-short-64")
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
    print("Calibration ..."),

    publisher_setup()
    print("Done !!!")

    # Start listening
    main()  