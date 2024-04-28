import os
import re
import sqlite3
import webbrowser
from engine.commands import speak
from engine.config import ASSISTANT_NAME
import pywhatkit as kit

# Import Database
connection = sqlite3.connect("lily.db")
cursor = connection.cursor()

def openCommand(query):
    query = query.replace(ASSISTANT_NAME, "")
    query = query.replace("open", "")
    query.lower()

    app_name = query.strip()

    if app_name != "":

        try:
            cursor.execute(
                'SELECT path FROM sys_command WHERE name IN (?)', (app_name,))
            results = cursor.fetchall()

            if len(results) != 0:
                speak("Opening "+query)
                os.startfile(results[0][0])

            elif len(results) == 0: 
                cursor.execute(
                'SELECT url FROM web_command WHERE name IN (?)', (app_name,))
                results = cursor.fetchall()
                
                if len(results) != 0:
                    speak("Opening "+query)
                    webbrowser.open(results[0][0])

                else:
                    speak("Opening "+query)
                    try:
                        os.system('start '+query)
                    except:
                        speak("not found")
        except:
            speak("some thing went wrong")


    # if query!= "":
    #     speak("opening" +query)
    #     os.system("start" +query)

    # else:
    #     speak("Command not found!")

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