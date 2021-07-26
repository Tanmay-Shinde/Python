import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia

listener = sr.Recognizer()
engine = pyttsx3.init()
def talk(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    try:
        with sr.Microphone() as source:
            voice =listener.listen(source)
            command =listener.recognize_google(voice)
            command = command.lower()
            if command :
                command = 'Sorry I did not get you there'
            elif 'nexus' in command:
                command = command.replace('nexus','')
                command = command.trim()

    except:
        command = 'Sorry I did not get you there'

    return command

def run_nexus():
    engine.say('Hey there. This is Nexus at your service.')
    engine.say('What can I do for you?')
    engine.runAndWait()
    command = take_command()
    if 'play' in command:
        song = command.replace('play','')
        print('playing '+song)
        talk('playing '+song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        print(time)
        talk('Current time is - '+time)
    elif 'who is' in command:
        inforeq = command.replace('who is','')
        info = wikipedia.summary(inforeq, 2)
        print(info)
        talk(info)
    elif 'tell me about' in command:
        inforeq = command.replace('tell me about', '')
        info = wikipedia.summary(inforeq, 2)
        print(info)
        talk(info)
    elif 'tell me something about' in command:
        inforeq = command.replace('tell me something about', '')
        info = wikipedia.summary(inforeq, 2)
        print(info)
        talk(info)

run_nexus()