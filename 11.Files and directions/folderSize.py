import os

allBytes = 0

for dirPath, dirnames, filenames in os.walk('./Resources/fifth/TestFolder'):
    if dirnames == []:
        for fileName in filenames:
            allBytes += os.stat(dirPath + '/' + fileName).st_size
print(allBytes / (1024*1024))