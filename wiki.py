import webbrowser #for opening up wikipedia 
import wikipedia
import pyttsx3

alexa = pyttsx3.init()
voices = alexa.getProperty('voices')
alexa.setProperty('voice', voices[1].id)

def talk(text):
    alexa.say(text)
    alexa.runAndWait()

def wikiSearch(go):
    print(go)
    try:
        result  = wikipedia.summary(go)
        print(result)
        talk(result)
        
            
    except Exception as e:
        print("not specific enough")
        pass

def main():
    go = input("What do you want to look up on Wikipedia? ")
    wikiSearch(go)

if __name__ == "__main__":
    main()
