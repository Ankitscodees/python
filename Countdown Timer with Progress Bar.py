import time
from tqdm import tqdm

def countdown_timer(seconds):
    for i in tqdm(range(seconds), desc="Counting down"):
        time.sleep(1)
    print("\nTime's up!")

# Countdown for 10 seconds
countdown_timer(10)
