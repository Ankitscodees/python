import time
from datetime import datetime
import winsound  # For Windows. Use `playsound` or similar libraries for other platforms.

def alarm_clock(set_alarm_time):
    print(f"Alarm set for {set_alarm_time}.")
    while True:
        current_time = datetime.now().strftime("%H:%M:%S")
        if current_time == set_alarm_time:
            print("Wake up! It's time!")
            for _ in range(5):  # Beep 5 times as an alarm
                winsound.Beep(1000, 1000)  # Frequency: 1000Hz, Duration: 1000ms
            break
        time.sleep(1)  # Wait for a second before checking the time again

# Main program
print("Welcome to the Alarm Clock!")
alarm_time = input("Enter the alarm time in HH:MM:SS format (24-hour): ")
alarm_clock(alarm_time)
