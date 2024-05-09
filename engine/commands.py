import pyttsx3
import speech_recognition as spchr
import eel
import time


def speak(text):
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    engine.setProperty('rate', 174)
    eel.DisplayMessage(text)
    engine.say(text)
    engine.runAndWait()


def takeCommand():
    recog = spchr.Recognizer()
    with spchr.Microphone() as source:
        print('Listening...')
        eel.DisplayMessage('Listening...')
        recog.pause_threshold = 1
        recog.adjust_for_ambient_noise(source)

        audio = recog.listen(source, 10, 6)
    try:
        print('Recognizing...')
        eel.DisplayMessage('Recognizing...')
        query = recog.recognize_google(audio, language='en-us')
        print(f"user said: {query}")
        eel.DisplayMessage(query)
    except Exception as e:
        return ""
    return query.lower()

@eel.expose
def allCommands(message=1):
    if message == 1:
        query = takeCommand()
        print(query)
    else: 
        query = message

    try:
        if "open" in query:
            from engine.features import openCommand
            openCommand(query)

        elif "on youtube" in query:
            from engine.features import playYoutube
            playYoutube(query)

        else:
            print("Something wrent wrong...")
    except:
        print("Something went wrong!")      
    eel.Showhood()