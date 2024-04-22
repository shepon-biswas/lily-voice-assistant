import pyttsx3
import speech_recognition as spchr
import eel


def speak(text):
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    engine.setProperty('rate', 174)

    engine.say(text)
    engine.runAndWait()

@eel.expose
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
        speak(query)
        eel.Showhood()
    except Exception as e:
        return ""
    return query.lower()


# text = takeCommand()

# speak(text)