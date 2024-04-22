import os
from engine.commands import speak
from engine.config import ASSISTANT_NAME


def openCommand(query):
    query = query.replace(ASSISTANT_NAME, "")
    query = query.replace("open", "")
    query.lower()

    if query!= "":
        speak("opening" +query)
        os.system("start" +query)
    else:
        speak("Command not found!")

# def handle_command(query):
#     if "open" in query:
#         openCommand(query)
#     else:
#         print("Error", query)