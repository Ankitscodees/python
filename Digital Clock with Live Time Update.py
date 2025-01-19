import time
import os

def digital_clock():
    while True:
        current_time = time.strftime("%H:%M:%S")
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f"Current Time: {current_time}")
        time.sleep(1)

digital_clock()
