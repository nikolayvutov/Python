inputFile = open('./Resources/first/Input.txt')
lines = inputFile.readlines()
linesCount = len(lines)
outputFile = open('./Resources/first/Output.txt', 'w')

for i in range(0, linesCount):
    if i % 2 == 1:
        currentLine = lines[i]
        outputFile.write(currentLine)

inputFile.close()
outputFile.close()
