import pyttsx3
import speech_recognition as spchr


def speak(text):
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    engine.setProperty('rate', 174)

    engine.say(text)
    engine.runAndWait()

def takeCommand():
    recog = spchr.Recognizer()
    with spchr.Microphone() as source:
        print('Listening...')
        recog.pause_threshold = 1
        recog.adjust_for_ambient_noise(source)

        audio = recog.listen(source, 10, 6)
    try:
        print('Recognizing...')
        query = recog.recognize_google(audio, language='en-us')
        print(f"user said: {query}")
    except Exception as e:
        return ""
    return query.lower()


text = takeCommand()

speak(text)