from settings import menu

class commandControl:
    def __init__(self, ss, sr):
        self.ss = ss        # Speech Synthiser 
        self.sr = sr        # Speech Recognizer
        self.cmds = {
    'greetings': self.sayHi,
    'menu': self.sayMenu,
    'bill': self.sayBill,
    'call': self.sayComing,
    'order': self.getOrder,
    'not_understand': self.notUnderstand,
    'none': self.none
}

 
    def do(self, cmd):
        ret = ""
        if (cmd in self.cmds):
            print(self.cmds[cmd])
            ret = self.cmds[cmd]()
        if ret:
            return ret

            

    def sayHi(self):
        self.ss.say("Привет, я робот Валли!")
    
    def sayMenu(self):
        text = "Мы подаем "
        for i in range(len(menu)):
            text += menu[i] + ", "
        text += "."
        self.ss.say(text)

    def sayBill(self):
        text="Ваш счет "
        text += "310 рублей."
        self.ss.say(text)


    def getOrder(self):
        listen = True
        text = ""
        while listen:
            text = self.sr.recognize().lower()
            if ("все" in text):
                self.ss.say("На этом все?")
                if ("да" in self.sr.recognize().lower):
                    listen = False
        
    def sayComing(self):
        self.ss.say("Я еду!")

    def notUnderstand(self):
        self.ss.say("Я не понимаю о чем вы говорите.")
    
    def none(self):
        self.ss.say("Я не могу понять, что вы сказали.")