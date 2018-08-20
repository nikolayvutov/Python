import re

text = input()
words = re.findall(r"[\w']+", text)
l = {}
uniq = []

for i in words:
    if i == i[::-1]:
        uniq.append(i)

uniq = sorted(uniq)
print(', '.join(uniq))