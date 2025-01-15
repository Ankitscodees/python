import random
import time
import os

def matrix_rain():
    columns = os.get_terminal_size().columns
    chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789@#$%&*"
    drops = [0] * columns

    while True:
        print("".join(random.choice(chars) if random.random() > 0.95 else " " for _ in range(columns)))
        drops = [drop + 1 if drop < random.randint(1, 20) else 0 for drop in drops]
        time.sleep(0.05)
        os.system('cls' if os.name == 'nt' else 'clear')

matrix_rain()
