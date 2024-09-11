import time
import os

delay = 0.03
def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def anim():
    file = open("combine3.txt", "r", encoding="utf-8")
    content = file.read()
    frames = content.split("---FRAME---")

    for i, frame in enumerate(frames):
        print(frame.strip())
        time.sleep(delay)
        clear_console()
anim()
