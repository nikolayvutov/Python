import re

text = input()

pattern = r'\b[A-Z][a-z]+ [A-Z][a-z]+\b'

match = re.search(pattern, text)

print(match.group(0))