import speech_recognition as sr
import pyttsx3
import datetime
import pywhatkit
import wikipedia
import pyjokes
import webbrowser
from tkinter import *
import threading
from websearch import *
from wiki import *
from PIL import ImageTk, Image

listener = sr.Recognizer()
alexa = pyttsx3.init()
voices = alexa.getProperty('voices')
alexa.setProperty('voice', voices[1].id)

def talk(text):
    alexa.say(text)
    alexa.runAndWait()


def take_command():
    while(True):
        try:
            with sr.Microphone() as source:
                talk('listening')
                print('listening...')
                voice = listener.listen(source)
                command = listener.recognize_google(voice)
                command = command.lower()
                
                if 'crystal' in command:
                    command = command.replace('crystal ', '', 1)
                    break
                
        except:
            pass
    return command


def run_alexa():
    phrase = take_command()
    if 'youtube' in phrase:
        phrase=phrase.replace('youtube ', '', 1)
        youSearch(phrase)
    elif 'google' in phrase:
        phrase=phrase.replace('google ', '', 1)
        googSearch(phrase)
    elif 'wikipedia' in phrase:
        phrase=phrase.replace('wikipedia ', '', 1)
        wikiSearch(phrase)
    elif 'time' in phrase:
        time = datetime.datetime.now().strftime('%I:%M %p')
        print(time)
        talk('Current time is ' + time)
    elif 'play' in phrase:
        song = phrase.replace('play', '')
        talk('playing ' + song)
        pywhatkit.playonyt(song)
    elif 'tell me about' in phrase:
        look_for = phrase.replace('tell me about', '')
        info = wikipedia.summary(look_for, 1)
        print(info)
        talk(info)
    elif 'joke' in phrase:
        talk(pyjokes.get_joke())
    elif 'stop' in phrase:
        exit()
    else:
        talk('I did not get it but I am going to search it for you')
        pywhatkit.search(phrase)
        
    
def runBack():
    print("running back\n")
    while(True):
        run_alexa()
    
def main():
    runBack()

if __name__ == '__main__':
    main()
