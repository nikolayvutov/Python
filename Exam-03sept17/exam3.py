import re

find = r'^([A-Za-z]+) ([A-Za-z]+)'
ignore = r'[^A-Za-z0-9]'


first = input()
second = input()

f = []
s = []
third = []

regex = re.findall(find, first)
f.append(regex)

second_regex = re.findall(find, second)
s.append(second_regex)

trash = re.findall('\w', second)
third.append(trash)

print(f)
print(s)