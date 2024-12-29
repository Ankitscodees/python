import time
import sys

def progress_bar(duration=5):
    total_steps = 50
    for step in range(total_steps + 1):
        percent = (step / total_steps) * 100
        bar = '#' * step + '-' * (total_steps - step)
        sys.stdout.write(f"\r[{bar}] {percent:.2f}%")
        sys.stdout.flush()
        time.sleep(duration / total_steps)
    print("\nTask Complete!")

progress_bar(10)  # 10-second progress bar
