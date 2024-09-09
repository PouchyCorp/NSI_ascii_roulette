import os
import time
from ascii_magic import AsciiArt

delay = 0.1

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def animation():

    script_dir = os.path.dirname(os.path.abspath(__file__))
    image_folder = os.path.join(script_dir, 'anim4')

    for filename in os.listdir(image_folder):
        if filename.endswith('.png') or filename.endswith('.jpg'):
            image_path = os.path.join(image_folder, filename)
            my_art = AsciiArt.from_image(image_path)
            my_art.to_terminal(columns=150)
            time.sleep(delay)
            clear_console()

animation()