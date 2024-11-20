import re

text = "Python is fun! 🐍😊"
emojis = re.findall(r'[^\w\s,]', text)

print("Detected Emojis:", emojis)
