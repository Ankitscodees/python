import random

def math_quiz():
    print("Welcome to the AI Math Quiz Game!")
    score = 0
    rounds = int(input("How many rounds would you like to play? "))
    
    for i in range(1, rounds + 1):
        num1 = random.randint(1, 20)
        num2 = random.randint(1, 20)
        operation = random.choice(["+", "-", "*"])
        
        if operation == "+":
            correct_answer = num1 + num2
        elif operation == "-":
            correct_answer = num1 - num2
        else:
            correct_answer = num1 * num2
        
        print(f"\nRound {i}: What is {num1} {operation} {num2}?")
        try:
            user_answer = int(input("Your answer: "))
            if user_answer == correct_answer:
                print("Correct!")
                score += 1
            else:
                print(f"Wrong! The correct answer was {correct_answer}.")
        except ValueError:
            print("Invalid input. Please enter a number.")
    
    print(f"\nGame Over! You scored {score}/{rounds}. Thanks for playing!")

# Run the math quiz game
math_quiz()
