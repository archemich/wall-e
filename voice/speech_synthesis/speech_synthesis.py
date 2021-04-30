import pyttsx3
from settings import voicepack, rate, volume
class SpeechSynthesiser:
    def __init__(self):
        self.tts = pyttsx3.init()
        self.tts.setProperty('voice', voicepack)
        self.tts.setProperty('rate', rate) 
        self.tts.setProperty('volume', volume) 

    def say(self, text):
        self.tts.say(text)
        self.tts.runAndWait()
        