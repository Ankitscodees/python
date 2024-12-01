import time

# Sample text for the typing test
sample_text = "The quick brown fox jumps over the lazy dog."

def typing_speed_test():
    print("\nTyping Speed Test!")
    print("Type the following text as quickly and accurately as you can:")
    print(f"\n{sample_text}\n")
    
    input("Press Enter when you are ready to start...")
    start_time = time.time()
    
    typed_text = input("\nType here: ")
    end_time = time.time()
    
    # Calculate typing speed and accuracy
    time_taken = end_time - start_time
    words_per_minute = len(typed_text.split()) / (time_taken / 60)
    accuracy = sum(1 for a, b in zip(sample_text, typed_text) if a == b) / len(sample_text) * 100

    print(f"\nTime Taken: {time_taken:.2f} seconds")
    print(f"Words Per Minute: {words_per_minute:.2f}")
    print(f"Accuracy: {accuracy:.2f}%")

# Run the typing speed test
typing_speed_test()
