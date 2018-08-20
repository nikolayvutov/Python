inputFile = open('./Resources/second/Input.txt')
outputFile = open('./Resources/second/Output.txt', 'w')

allInputLines = inputFile.readlines()
numberOfLines = len(allInputLines)

for i in range(numberOfLines):
    currentLine = allInputLines[i]
    outputFile.write(str(i + 1) + '. ' + currentLine)

inputFile.close()
outputFile.close()