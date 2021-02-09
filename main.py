from speech_recog.speech_recog import SpeechRecognizer
from speech_synthesis.speech_synthesis import SpeechSynthesiser
import commands

sr = SpeechRecognizer()
sr.calibrate()

ss = SpeechSynthesiser()

opts = {"cmds": {
    "greetings": ("привет", "здорово"),
    "none": ()
    }}

def recognizeCommand(text):
    print(text)
    for cmd, verbose_cmds in opts['cmds'].items():
        for verbose_cmd in verbose_cmds:
            if(verbose_cmd in text):
                return cmd
    
    return "none"


def do_command(cmd):
    ss.say(commands.cmds.get(cmd, 0))


if __name__ == "__main__":
    while True:
        do_command(recognizeCommand(sr.recognize().lower()))
        