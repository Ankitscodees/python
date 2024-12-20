import random

def magic_8_ball():
    responses = [
        "Yes, definitely!",
        "It is certain.",
        "Ask again later.",
        "Better not tell you now.",
        "Don't count on it.",
        "My sources say no.",
    ]
    question = input("Ask the Magic 8-Ball a question: ")
    print("Thinking...")
    time.sleep(1)
    print("Magic 8-Ball says:", random.choice(responses))

magic_8_ball()
