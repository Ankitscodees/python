from datetime import datetime

def display_binary_clock():
    now = datetime.now()
    hour = f"{now.hour:06b}"  # Binary representation of the hour
    minute = f"{now.minute:06b}"  # Binary representation of the minute
    second = f"{now.second:06b}"  # Binary representation of the second
    
    print("\nBinary Clock:")
    print(f"Hour   : {hour}")
    print(f"Minute : {minute}")
    print(f"Second : {second}")
    print("Tip: 0 = Off, 1 = On")

while True:
    display_binary_clock()
    input("\nPress Enter to update time...")
