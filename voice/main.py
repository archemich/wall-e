from speech_recog.speech_recog import SpeechRecognizer
from speech_synthesis.speech_synthesis import SpeechSynthesiser
from commands import commandControl

sr = SpeechRecognizer()
sr.calibrate()

ss = SpeechSynthesiser()

cmdCtrl = commandControl(ss, sr)
#INSTALL ESPEAK, FLACK
# sudo apt update 
# sudo apt install python-espeak

# Работает приоритет. Команды выше сработают первыми.
opts = {"cmds": {
    "greetings": ("привет", "здорово"),
    "menu": ("меню"),
    'bill': ("счет", "счёт"),
    'order': ("заказ", "заказать"),
    'call': ("официант", "валли"),
    "none": (""), # На случай если робот распознает пустую строку.
    }}

# Проверка наличия вербальных команд в голосовом запросе пользователя. 
# Если слово найдено - возвращает имя команды, иначе возвращает имя команды "not_understand"
def recognizeCommand(text):
    print(text)
    # cmd - слово слева, verbose_cmds - список слов справа в opts
    for cmd, verbose_cmds in opts['cmds'].items(): 

        # Это позволяет писать в opts одну вербальную команду
        if (isinstance(verbose_cmds, tuple) == False): 
            verbose_cmds = list([verbose_cmds])

        for verbose_cmd in verbose_cmds:
            if(verbose_cmd in text):
                return cmd
    
    return "none"


def do_command(cmd):
    cmdCtrl.do(cmd)

if __name__ == "__main__":
    while True:
        do_command(recognizeCommand(sr.recognize().lower()))
        