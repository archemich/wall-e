import os
import socket
import errno
import time
import rospy
from rospy.client import DEBUG
from std_msgs.msg import String, Float32
from socket import error as SocketError
from playsound import playsound

import RPi.GPIO as GPIO
from adafruit_servokit import ServoKit
global moveAngle
moveAngle = 0


DEBUG = 1

def on_board_systems_check():
    #pubVoice.publish("play robo-short-64")
    plstr = "/home/ubuntu/Project-WALLE/catkin_ws/src/walle/scripts/sounds/robo-short-64.wav"
    playsound(plstr)
    global pubServos
    pubServos.publish('S 0') # Setup function call
    

def publisher_setup():
    global pubVoice
    pubVoice = rospy.Publisher("voice", String, queue_size=1)
    #base message format [angle, distance from origin]
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
        if (int(parsedLine[1]) > (moveAngle+5)) or (int(parsedLine[1]) < (moveAngle-5)) or (int(parsedLine[2]) == 0):
            pubBase.publish(mess)
            rospy.loginfo(" | ".join(parsedLine))
            
            # if not(int(parsedLine[2]) == 0):
            #     pubVoice.publish("play robo-short-56")

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
    print("done !!!")
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
    if DEBUG == 1: on_board_systems_check()

    # Start listening
    main()  


    # kit.servo[9].angle = 90
    
    # head = 9
	# kit.servo[head].angle = 0
	# for i in range(0,180,3):
	# 	kit.servo[head].angle = i
	# 	time.sleep(0.02)

	# for i in range(180,0,-3):
	# 	kit.servo[head].angle = i
	# 	time.sleep(0.02)



    # left = int(kit.servo[handLeft].angle) 	# Левая 
	# 	for i in range(left, 0,-3):
	# 		kit.servo[handLeft].angle = i 
	# 		time.sleep(0.01)
		
	# 	right = int(kit.servo[handRight].angle)	# Правая
	# 	for i in range(right, 180,3):
	# 		kit.servo[handRight].angle = i
	# 		time.sleep(0.01)

	# 	# Руки вниз
	# 	for i in range(0, 180, 3): 			   	# Левая 
	# 		kit.servo[handLeft].angle = i 
	# 		time.sleep(0.01)

	# 	for i in range(180, 0, -3):			   	# Правая
	# 		kit.servo[handRight].angle = i 
	# 		time.sleep(0.01)

	# 	# обратно в середину

	# 	for i in range(180, 90, -3):		    # Левая 
	# 		kit.servo[handLeft].angle = i 
	# 		time.sleep(0.01)

	# 	for i in range(0, 90, 3):				# Правая
	# 		kit.servo[handRight].angle = i 
	# 		time.sleep(0.01)