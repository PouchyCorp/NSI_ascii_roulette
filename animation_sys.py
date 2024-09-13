import time
import os

delay = 0.06
def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def anim(anim_name : str):
    file = open(f"{anim_name}.txt", "r", encoding="utf-8")
    content = file.read()
    frames = content.split("---FRAME---")

    for frame in frames:
        print(frame.strip())
        time.sleep(delay)
        clear_console()