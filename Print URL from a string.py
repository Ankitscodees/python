# Python program to print URL from a string
import re

# Getting strings as input from the user 
myStr = input('Enter string : ')

# Finding all URLS from the string 
urlRegex = r"(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'\".,<>?«»""'']))"

allUrls = re.findall(urlRegex,myStr)	

print("All URLs are ", [url[0] for url in allUrls])
