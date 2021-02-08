import speech_recognition as sr
from settings import *


# obtain audio from the microphone
r = sr.Recognizer()

with sr.Microphone(device_index = dev_index) as source:
    print("Say something!")
    audio = r.listen(source)

# recognize speech using Google Speech Recognition
try:
    print(r.recognize_google(audio, language = "ru-RU"))
except sr.UnknownValueError:
    print("Google Speech Recognition could not understand audio")
except sr.RequestError as e:
    print("Could not request results from Google Speech Recognition service; {0}".format(e))