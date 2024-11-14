import re

text = "Hello World\nhello world\nHELLO WORLD"

# Case-insensitive search
pattern = "hello"
matches = re.findall(pattern, text, re.IGNORECASE)
print("Case-insensitive matches:", matches)

# Multi-line search
pattern_multiline = "^hello"
matches_multiline = re.findall(pattern_multiline, text, re.IGNORECASE | re.MULTILINE)
print("Multi-line matches:", matches_multiline)
