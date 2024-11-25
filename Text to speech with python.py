import pyttsx3

# Initialize the text-to-speech engine
engine = pyttsx3.init()

# Text to speak
text = "Python programming is fun and versatile!"

# Set speaking rate and voice (optional)
engine.setProperty('rate', 150)  # Speed of speech
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)  # Change index for different voices

# Speak the text
engine.say(text)
engine.runAndWait()
