import time

def stopwatch():
    print("Welcome to the Stopwatch!")
    print("Press Enter to start the stopwatch, Enter again to stop it, and type 'quit' to exit.")
    
    while True:
        command = input("\nPress Enter to start or type 'quit' to exit: ").strip().lower()
        if command == "quit":
            print("Goodbye!")
            break
        
        print("Stopwatch started. Press Enter to stop.")
        start_time = time.time()
        input()
        end_time = time.time()
        
        elapsed_time = end_time - start_time
        print(f"Elapsed Time: {elapsed_time:.2f} seconds")

# Run the stopwatch
stopwatch()
