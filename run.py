import multiprocessing

# To run Alexa
def startAlexa():
    print("Process 1 is running...")
    from main import start
    start()

# To run hotword
def listenHotWord():
    print("Process 2 is running...")
    from engine.features import hotword
    hotword()

# start both process
if __name__ == '__main__':
    process1 = multiprocessing.Process(target=startAlexa)
    process2 = multiprocessing.Process(target=listenHotWord)
    process1.start()
    process2.start()
    process1.join()

    if process2.is_alive():
        process2.terminate()
        process2.join()
    print("system stop")