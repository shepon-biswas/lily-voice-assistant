import os
import re
import sqlite3
import struct
import time
import webbrowser

import pyaudio
from engine.commands import speak
from engine.config import ASSISTANT_NAME
import pywhatkit as kit
from engine.helper import extractYtTerm
import pvporcupine
from hugchat import hugchat


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


def playYoutube(query):
    searchTerm = extractYtTerm(query)
    if searchTerm:
        speak("Playing "+searchTerm+" on youtube")
        kit.playonyt(searchTerm)
    else:
        speak("Sorry, I couldn't understand the YouTube search term.")

# Hot Word Wake up Function
def hotword():
    porcupine=None
    paud=None
    audio_stream=None
    try:
       
        # pre trained keywords    
        porcupine=pvporcupine.create(keywords=["jarvis","alexa"]) 
        paud=pyaudio.PyAudio()
        audio_stream=paud.open(rate=porcupine.sample_rate,channels=1,format=pyaudio.paInt16,input=True,frames_per_buffer=porcupine.frame_length)
        
        # loop for streaming
        while True:
            keyword=audio_stream.read(porcupine.frame_length)
            keyword=struct.unpack_from("h"*porcupine.frame_length,keyword)

            # processing keyword comes from mic 
            keyword_index=porcupine.process(keyword)

            # checking first keyword detetcted for not
            if keyword_index>=0:
                print("hotword detected")

                # pressing shorcut key win+j
                import pyautogui as autogui
                autogui.keyDown("win")
                autogui.press("j")
                time.sleep(2)
                autogui.keyUp("win")
                
    except:
        if porcupine is not None:
            porcupine.delete()
        if audio_stream is not None:
            audio_stream.close()
        if paud is not None:
            paud.terminate()

# HugChat- AI chat box
def split_into_sentences(text):
    # Use regular expression to split text into sentences based on punctuation
    sentences = re.split(r'(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?|\!)\s', text)
    return sentences

def chatBot(query):
    user_input = query.lower()
    chatbot = hugchat.ChatBot(cookie_path="engine\cookies.json")
    ChatID = chatbot.new_conversation()
    chatbot.change_conversation(ChatID)
    botResponse =  chatbot.chat(user_input)
    response_to_string  = str(botResponse)
    # Split the response into sentences
    sentences = split_into_sentences(response_to_string)
    
    # Select only the first 5 sentences
    first_3_sentences = ' '.join(sentences[:3])
    
    print(first_3_sentences)
    speak(first_3_sentences)
    return first_3_sentences

