text = input().lower()
word = input().lower()

counter = 0

try:
    index = text.find(word)
except:
    index = -1

while index != -1:
    try:
        index = text.find(word, index + 1)
    except:
        index = -1

    counter += 1

print(counter)