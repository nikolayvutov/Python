import re

n = input()

while n != 'Traincode!':
    isValid = True
    if re.search(r'^(<\[[^A-Za-z0-9]*?\]\.)+(\.\[[A-Za-z0-9]*\]\.)*$', n) != None:
        print(n)
    n = input()