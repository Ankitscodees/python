import random

def random_color_generator():
    print("Random Color Generator 🎨")
    for _ in range(5):
        color = "#{:06x}".format(random.randint(0, 0xFFFFFF))
        print(f"Generated Color: {color}")

random_color_generator()
