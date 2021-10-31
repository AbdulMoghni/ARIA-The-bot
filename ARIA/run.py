
from PyQt5 import QtWidgets, QtGui,QtCore
from PyQt5.QtGui import QMovie
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.uic import loadUiType
import pyttsx3
import speech_recognition as sr
import os
import time
import wikipedia
import webbrowser
import datetime



flags = QtCore.Qt.WindowFlags(QtCore.Qt.FramelessWindowHint)

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)
engine.setProperty('rate',250)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wish():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour <12:
        speak("Good morning")
    elif hour>=12 and hour<18:
        speak("Good Afternoon")
    else:
        speak("Good night")
    speak("I am ARIA the bot sir , how may I help you")

class mainT(QThread):
    def __init__(self):
        super(mainT,self).__init__()
    
    def run(self):
        self.ARIA()
    
    def STT(self):
        R = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listning...........")
            audio = R.listen(source)
        try:
            print("Recog......")
            text = R.recognize_google(audio,language='en-in')
            print(">> ",text)
        except Exception:
            return "none"
            
        text = text.lower()
        return text

    def ARIA(self):
        wish()
        while True:
            
            self.query = self.STT()
            if 'activate' in self.query:
                self.query=self.query.replace("activate","")
                search=self.query
                if 'bye' in self.query:
                    sys.exit()
                elif 'open google' in self.query:
                    webbrowser.open('www.google.co.in')
                    speak("opening google")
                elif 'youtube' in self.query:
                    search=search.replace("youtube","")
                    webbrowser.open(f'https://www.youtube.com/results?search_query={search}')
                elif 'time' in self.query:
                    strTime = datetime.datetime.now().strftime("%H:%M:%S")    
                    speak(f"Sir, the time is {strTime}")
                
                elif 'code' in self.query:
                    codePath = "C:\\Users\\TANWEER\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
                    os.startfile(codePath)
                
                elif 'music' in self.query:
                    codePath = "C:\\Users\\TANWEER\\AppData\\Local\\Programs\\Resso\\Resso.exe"
                    os.startfile(codePath)
            
            
            
                elif 'discord' in self.query:
                   
                    codePath = "C:\\Users\\TANWEER\\AppData\\Local\\Discord\\Update.exe --processStart Discord.exe"
                    os.startfile(codePath)
                
                
                
                
                elif 'virtual world' in self.query:
               
                    codePath = "C:\\Program Files (x86)\\VMware\\VMware Workstation\\vmware.exe"
                    os.startfile(codePath)
                
                
                elif 'game' in self.query:
                    
                    codePath = "E:\\My Games\\Blair Witch\\Blairwitch.exe"
                    os.startfile(codePath)
                
                
                
                elif 'wikipedia' in self.query:          
                    sd=self.query
                    sd=sd.replace("wikipedia","")
                    result=wikipedia.summary(sd,6)
                    print(result)
                    speak(result)
                
                
                
                elif 'none' not in self.query:
                    webbrowser.open(f'https://www.google.com/search?q={search}')
                    
                   
            
                 























FROM_MAIN,_ = loadUiType(os.path.join(os.path.dirname(__file__),"./scifi.ui"))

class Main(QMainWindow,FROM_MAIN):
    def __init__(self,parent=None):
        super(Main,self).__init__(parent)
        self.setupUi(self)
        self.setFixedSize(1920,1080)
        self.label_7 = QLabel
        self.exitB.setStyleSheet("background-image:url(./lib/exit - Copy.png);\n"
        "border:none;")
        self.exitB.clicked.connect(self.close)
        self.setWindowFlags(flags)
        Dspeak = mainT()
        self.label_7 = QMovie("./lib/gifloader.gif", QByteArray(), self)
        self.label_7.setCacheMode(QMovie.CacheAll)
        self.label_4.setMovie(self.label_7)
        self.label_7.start()

        self.ts = time.strftime("%A, %d %B")

        Dspeak.start()
        self.label.setPixmap(QPixmap("./lib/bgimage1234.png"))
        self.label_5.setText("<font size=8 color='green' background color='black'>"+self.ts+"</font>")
        self.label_5.setFont(QFont(QFont('Acens',8)))


app = QtWidgets.QApplication(sys.argv)
main = Main()
main.show()
exit(app.exec_())