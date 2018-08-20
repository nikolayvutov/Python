inputFile = open('./Resources/third/text.txt')
outputFile = open('./Resources/third/words.txt')

text = inputFile.readlines()[0]
word = outputFile.readlines()[0].split(' ')
print(word[0])

count = 0

for i in text:
    if word[0] in text:
        count += 1

print(count)




inputFile.close()
outputFile.close()