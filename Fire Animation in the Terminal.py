import random
import time
import os

def fire_animation():
    fire_chars = ['.', ':', ';', '*', '!', '$', '@', '#']
    while True:
        fire = ''.join(random.choices(fire_chars, k=80))
        print(fire)
        time.sleep(0.1)
        os.system('cls' if os.name == 'nt' else 'clear')

fire_animation()
