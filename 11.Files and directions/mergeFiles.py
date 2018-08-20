import re

firstInputFile = open('./Resources/fourth/FileOne.txt')
secondInputFile = open('./Resources/fourth/FileTwo.txt')

firstLines = firstInputFile.readlines()
firstLinesCount = len(firstLines)
secondLines = secondInputFile.readlines()
secondLinesCount = len(secondLines)

outputFile = open('./Resources/fourth/Output.txt', 'w')
t = []

for i in range(0, firstLinesCount):
    curr = firstLines[i]
    t.append(curr)

for i in range(0, secondLinesCount):
    curr = secondLines[i]
    t.append(curr)

work = []
for i in sorted(t):
    work += re.findall(r'[0-9]', i)
print(work)

for w in work:
    outputFile.write('{}\n'.format(w))

firstInputFile.close()
secondInputFile.close()
outputFile.close()