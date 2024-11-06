from random import choice

# A function that randomizes between 0 and 1
def coin_toss():
    states = {1: "Heads", 0: "Tails"}
    one_or_zero = choice([0, 1])
    result = states[one_or_zero]
    print(result)

# Example run
coin_toss()
