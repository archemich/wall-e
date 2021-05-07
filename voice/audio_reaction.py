import rospy
from std_msgs.msg import String
import playsound
from espeak import espeak


def say(message):
    spMessage = message.split(" ")
    if spMessage[0] == "talk":
        pass
    elif spMessage[0] == "play":
        playsound("{}.wav".format(spMessage[1]))




if __name__ == '__main__': 
    rospy.init_node('voice')
    rospy.Subscriber("audio", String, say)
