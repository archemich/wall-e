#!/usr/bin/env python3
"""Simple test for a standard servo on channel 0 and a continuous rotation servo on channel 1."""
import time
import rospy
from adafruit_servokit import ServoKit
from std_msgs.msg import String
 
# Set channels to the number of servo channels on your kit.
# 8 for FeatherWing, 16 for Shield/HAT/Bonnet.
kit = ServoKit(channels=16)
head = 4
handRight = 1
handLeft = 7
hinge = 5
fingaLeft = 14
fingaRight = 15

def move_smth(data):
	rospy.loginfo(data.data)
	print(data.data)
	value = data.data
	value = value.split(" ")
	

	if value[0] == 'R':
		ang = int(value[1])
		portNumber = handRight
		ang = 180-ang
	elif value[0] == 'L':
		ang = int(value[1])
		portNumber = handLeft
	elif value[0] == 'T':
		if value[1] == 'R':
			if int(value[2]) == 1:
				ang = 180
			else:
				ang = 0
			portNumber = fingaRight
			# 	ang = 180-ang
		elif value[1] == 'L':
			if int(value[2]) == 1:
				ang = 180
			else:
				ang = 0
			portNumber = fingaLeft

	kit.servo[portNumber].angle = ang

	# for i in range(0, 180, 2):
	# 	kit.servo[portNumber].angle = i
	# 	time.sleep(0.01)
	# 	print("I like to move it move it", i, end='\r')
	# time.sleep(1)
	# for j in range(180, 0, -2):
	# 	kit.servo[portNumber].angle = j
	# 	time.sleep(0.01)
	# 	print("I like to move it move it", j, end='\r')


def move_hand(handNum):
	kit.servo[handNum].angle=0
	time.sleep(2)
	kit.servo[handNum].angle = 0
	# time.sleep(0.05)
	# kit.servo[handNum].angle = 80
	# time.sleep(0.05)
	# kit.servo[handNum].angle = 80


def hand_home(arm=0, hand=0):	
	if arm:
		kit.servo[handLeft].angle = 0 
		kit.servo[handRight].angle = 180
	else:
		kit.servo[handLeft].angle = 180
		kit.servo[handRight].angle = 0

	if hand:
		kit.servo[fingaLeft].angle = 0
		kit.servo[fingaRight].angle = 180
	else:
		kit.servo[fingaLeft].angle = 180
		kit.servo[fingaRight].angle = 0


def listen():
    rospy.init_node("servos")
    rospy.Subscriber("joints", String, move_smth)

    rospy.spin()


if __name__ == '__main__':
	hand_home(1, 0)
	listen()
