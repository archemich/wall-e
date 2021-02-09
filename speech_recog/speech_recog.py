import speech_recognition as sr
from settings import dev_index, recognition_language


class SpeechRecognizer:
    def __init__(self):
        self.r = sr.Recognizer()
        self. mic = sr.Microphone(device_index = dev_index)

    def calibrate(self):
        print("Идет калибровка...")
        with self.mic as source:
            self.r.adjust_for_ambient_noise(source)
        print("Калибровка окончена")


    def recognize(self):
        res = ""
        with self.mic as source:
            print("Say something!")
            audio = self.r.listen(source)

            # recognize speech using Google Speech Recognition
            try:
                res = self.r.recognize_google(audio, language = recognition_language)
            except sr.UnknownValueError:
                err = "Google Speech Recognition could not understand audio"
                print(err)
            except sr.RequestError as e:
                err = "Could not request results from Google Speech Recognition service; {0}".format(e)
                print(err)       
        return res     