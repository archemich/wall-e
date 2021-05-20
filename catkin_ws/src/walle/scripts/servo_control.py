#!/usr/bin/env python3
"""Simple test for a standard servo on channel 0 and a continuous rotation servo on channel 1."""
import time
import rospy
from adafruit_servokit import ServoKit
from std_msgs.msg import String
 
# Set channels to the number of servo channels on your kit.
# 8 for FeatherWing, 16 for Shield/HAT/Bonnet.
kit = ServoKit(channels=16)
# head = 9
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
	
	if value[0] == 'S':
		hand_home(1,1)
		return
	elif value[0] == 'R':
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

def hand_home(arm=0, hand=0):	
	if arm:
		# Руки вверх 
		for i in range(90, 0,-4):				# Левая и правая
			kit.servo[handLeft].angle = i
			kit.servo[handRight].angle = 180 - (i - 1);
			time.sleep(0.03)
		
		# Руки вниз
		for i in range(0, 180, 4): 			   	# Левая и правая
			kit.servo[handLeft].angle = i 
			kit.servo[handRight].angle = 180 - i;
			time.sleep(0.03)

		# обратно в середину
		for i in range(180, 90, -4):		    # Левая правая
			kit.servo[handLeft].angle = i 
			kit.servo[handRight].angle = 180 - (i - 1)
			time.sleep(0.03)

		# for i in range(90,0,-4):
		# 	kit.servo[handLeft].angle = i
		# 	kit.servo[handRight].angle = 0 + (180 - i*2)
		# 	time.sleep(0.03)


	else:
		kit.servo[handLeft].angle = 180
		kit.servo[handRight].angle = 0

	if hand:
		kit.servo[fingaLeft].angle = 180		# Левая 
		time.sleep(1)
		kit.servo[fingaLeft].angle = 0;
		time.sleep(1)
		kit.servo[fingaLeft].angle = 180

		head = 9
		for i in range(90,0,-3):
			kit.servo[head].angle = i
			time.sleep(0.02)

		for i in range(0,180,3):
			kit.servo[head].angle = i
			time.sleep(0.02)

		for i in range(180,90,-3):
			kit.servo[head].angle = i
			time.sleep(0.02)


		# kit.servo[fingaRight].angle = 0			# Правая
		# time.sleep(1)
		# kit.servo[fingaLeft].angle = 180
		# time.sleep(1)
		# kit.servo[fingaRight].angle = 0

	else:
		kit.servo[fingaLeft].angle = 180
		kit.servo[fingaRight].angle = 0


def listen():
    rospy.init_node("servos")
    rospy.Subscriber("joints", String, move_smth)

    rospy.spin()


if __name__ == '__main__':
	listen()
