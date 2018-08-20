censoredWords = input().split(', ')

text = input()

for word in censoredWords:
    text = text.replace(word, '*' * len(word))
print(text)