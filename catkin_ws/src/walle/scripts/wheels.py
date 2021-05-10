import time
import RPi.GPIO as GPIO
import rospy
from std_msgs.msg import String

def setup_gpio():
    GPIO.setwarnings(False)
    GPIO.cleanup()
    GPIO.setmode(GPIO.BCM)

    GPIO.setup(17, GPIO.OUT)
    GPIO.setup(22, GPIO.OUT)
    GPIO.setup(27, GPIO.OUT)
    GPIO.setup(10, GPIO.OUT)

    GPIO.output(17, GPIO.LOW)
    GPIO.output(22, GPIO.LOW)
    GPIO.output(27, GPIO.LOW)
    GPIO.output(10, GPIO.LOW)

def move(data):
    #change data input from messArr to data.data
    rospy.loginfo(data.data)
    value = data.data
    value = value.split(" ")
    # GPIO.output(17, GPIO.LOW)
    # GPIO.output(22, GPIO.LOW)
    # GPIO.output(27, GPIO.LOW)
    # GPIO.output(10, GPIO.LOW)
    ang = int(value[0])
    amp = int(value[1])
    if int(amp) > 50:
        if ang in range(75, 105):
            GPIO.output(17, GPIO.HIGH)
            GPIO.output(22, GPIO.HIGH)

        elif ang in range(0, 75)or ang in range(286, 360):
            GPIO.output(22, GPIO.HIGH)
            GPIO.output(10, GPIO.HIGH)
        elif ang in range(106, 256):
            GPIO.output(17, GPIO.HIGH)
            GPIO.output(27, GPIO.HIGH)
        elif ang in range(256, 286):
            GPIO.output(10, GPIO.HIGH)
            GPIO.output(27, GPIO.HIGH)
    else:
        GPIO.output(17, GPIO.LOW)
        GPIO.output(22, GPIO.LOW)
        GPIO.output(27, GPIO.LOW)
        GPIO.output(10, GPIO.LOW)
    # time.sleep(0.005)


def listen():
    rospy.init_node("wheels")
    
    rospy.Subscriber("base", String, move)

    rospy.spin()


if __name__ == '__main__':
    setup_gpio()
    listen()