#!/usr/bin/env python3
import rospy
from std_msgs.msg import String
from playsound import playsound
from espeak import espeak


def say(data):
    message = data.data
    rospy.loginfo(data.data)
    spMessage = message.split(" ")
    rospy.loginfo(spMessage)
    if spMessage[0] == "talk":
        pass
    elif spMessage[0] == "play":
        plstr = "/home/ubuntu/Project-WALLE/catkin_ws/src/walle/scripts/sounds/"+ spMessage[1]+".wav"
        rospy.loginfo(plstr)
        playsound(plstr)



def do():
    rospy.Subscriber("voice", String, say)
    rospy.spin()


if __name__ == '__main__': 
    rospy.init_node('voice_rec')
    do()
