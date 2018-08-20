import re

text = input()

patternForDashes = r'\+359-2-\d{3}-\d{4}\b'
patternForSpaces = r'\+359 2 \d{3} \d{4}\b'

matchOne = re.search(patternForSpaces, text)
matchTwo = re.search(patternForDashes, text)

print(matchOne.group(0))
print(matchTwo.group(0))