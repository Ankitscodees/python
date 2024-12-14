from pyfiglet import Figlet

def ascii_art_generator(text, font="slant"):
    figlet = Figlet(font=font)
    return figlet.renderText(text)

# Example usage
text = "Python Rocks"
print(ascii_art_generator(text))
