import time
from datetime import datetime

def digital_clock():
    print("Digital Clock (Press Ctrl+C to stop):")
    try:
        while True:
            now = datetime.now()
            current_time = now.strftime("%H:%M:%S")
            print(f"\rCurrent Time: {current_time}", end="")
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nClock Stopped. Have a great day!")

digital_clock()
