import re

text = input()

pattern = r'([a-z]+.[a-z]+[@][a-z]+.[a-z]+[.][a-z]+)\b'

match = re.findall(pattern, text)

for i in match:
    print(i)