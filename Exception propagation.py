def level_1():
    # Level 1 does not handle the exception, so it propagates further
    level_2()

def level_2():
    # Level 2 does not handle the exception, so it propagates further
    level_3()

def level_3():
    # Level 3 raises an exception
    raise ValueError("Something went wrong in level_3!")

try:
    # Start the function chain
    level_1()
except ValueError as e:
    # Handle the exception that was propagated
    print(f"Exception caught: {e}")
finally:
    print("Execution finished.")
