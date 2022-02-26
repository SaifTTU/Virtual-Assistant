from Youtube import*
import speech_recognition as sr
import pyttsx3
import datetime
import pywhatkit
import wikipedia
import pyjokes

listener = sr.Recognizer()
alexa = pyttsx3.init()
voices = alexa.getProperty('voices')
alexa.setProperty('voice', voices[1].id)


def talk(text):
    alexa.say(text)
    alexa.runAndWait()


def take_command():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            print(command)
            '''
            if 'alexa' in command:
                command = command.replace('alexa', '')
            '''
            
            phrase = "Youtube RickAsley for me"

            phrase = phrase.lower()
            if("youtube" in phrase):
                phrase = phrase.replace("youtube ","")

                print("searching youtube...")
                youSearch(phrase)
            if("weather" in phrase):
                degrees = int(90)
                celcius = 30
                celcius = int( (degrees-30)* (5/9) )
                response = "it's currently "
                high = 0
                low = 0
                #phrase = "Hey tell me the Weather celcius"
                phrase = input("Question ") 


                phrase = phrase.lower()

                #celcius = float(degrees−32*5/9)

                if( "weather" in phrase):
                if("celcius" in phrase):

                    response +=  str(celcius) + " degrees C°"
                elif("farenheight" in phrase):
                    response += (str(degrees)+ " degrees F°")
                else:
                    response += (str(degrees)+ " degrees F° and "+ str(celcius)+ " °C")
                response += " with high's reaching " + str(high)
                response += " and " 
                response += " with low's reaching " + str(low)
                print(response)
    except:
        pass
        #return command


def run_alexa():
    command = take_command()
    '''
    if 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        print(time)
        talk('Current time is ' + time)
    elif 'play' in command:
        song = command.replace('play', '')
        talk('playing ' + song)
        pywhatkit.playonyt(song)
    elif 'tell me about' in command:
        look_for = command.replace('tell me about', '')
        info = wikipedia.summary(look_for, 1)
        print(info)
        talk(info)
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    elif 'date' in command:
        talk('Sorry vaiya, I am in another relation')
    else:
        talk('I did not get it but I am going to search it for you')
        pywhatkit.search(command)
    '''

while True:
    run_alexa()
