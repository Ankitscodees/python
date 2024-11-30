import time

class Timer:
    def __init__(self, label="Code Block"):
        self.label = label

    def __enter__(self):
        self.start_time = time.time()
        print(f"{self.label} started...")
        return self  # Allow access to this context manager's instance

    def __exit__(self, exc_type, exc_val, exc_tb):
        end_time = time.time()
        print(f"{self.label} ended. Duration: {end_time - self.start_time:.4f} seconds")

# Using the custom context manager
with Timer("Loop Execution"):
    total = 0
    for i in range(1_000_000):
        total += i
    print(f"Total: {total}")
