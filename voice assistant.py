import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def talk(text):
    engine.say(text)
    engine.runAndWait()
    

def take_command():
    try:
        with sr.Microphone() as source:
            print('listening.....')
            talk('any help needed')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            print(command)

    except:
        pass
    return command


def intro():
    try:
        with sr.Microphone() as source1:
            talk('please tell your name')
            voice1 = listener.listen(source1)
            name = listener.recognize_google(voice1)
            name = name.lower()
            
    except:
        pass
    return name

def run_alexa():
    command = take_command()
    print(command)
    if 'who' in command:
        info = wikipedia.summary(command, 1)
        print(info)
        talk(info)
    if 'play' in command:
        song = command.replace('play', '')
        print('playing')
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        print('time is '+ time)
        talk('time is '+time)
    elif 'joke' in command:
        talk(pyjokes.get_joke())


def print_name():
    name = intro()
    print('hi ' + name)
    talk('hi ' + name)
    talk('I am Alex , your voice assistant')
    
def out():
    while True:
        run_alexa()  
        command = take_command()
        if command == 'no thanks':
            break  
print_name()
out()

