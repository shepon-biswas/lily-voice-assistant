import os
import eel

from engine.commands import *

def start():
    eel.init("layout") 
    os.system('start msedge.exe --app="http://localhost:8000/index.html"')
    eel.start('index.html', mode=None, host='localhost', block=True)
