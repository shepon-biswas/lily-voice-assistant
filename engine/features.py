import os
import re
from engine.commands import speak
from engine.config import ASSISTANT_NAME
import pywhatkit as kit


def openCommand(query):
    query = query.replace(ASSISTANT_NAME, "")
    query = query.replace("open", "")
    query.lower()

    if query!= "":
        speak("opening" +query)
        os.system("start" +query)

    else:
        speak("Command not found!")

def playYoutube(query):
    searchTerm = extractYtTerm(query)
    if searchTerm:
        speak("Playing "+searchTerm+" on youtube")
        kit.playonyt(searchTerm)
    else:
        speak("Sorry, I couldn't understand the YouTube search term.")


def extractYtTerm(command):
    pattern = r'play\s+(.*?)\s+on\s+youtube'
    match = re.search(pattern, command, re.IGNORECASE)
    return match.group(1) if match else None