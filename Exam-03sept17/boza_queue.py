import re

n = input().split(' ')

line = []
ans = []

while n[0] != '':
    if n[0] == 'ADD':
        line.append(n[1])
    elif n[0] == 'NEXT':
        ans.append(line[-1])
    elif n[0] == 'SKIP':
        line.pop(-1)
    elif n[0] == 'REM':
        if n[1] in line:
            name = n[1]
            line.remove(name)
    elif n[0] == 'CLEANUP':
        for i in line:
            if len(i) % 2 == 0:
                ans.append(i)
    elif n[0] == 'CLEANDOWN':
        for i in range(len(line)):
            if i % 2 == 0 and (len(line[i]) % 2 == 0):
                line.remove(line[i])
    n = input().split(' ')

line.sort(key=len)

for i in line:
    print(i)
