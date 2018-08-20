import re
word = input()
text = input()


pattern = r'[^.?!]*(?<=[.?\s!])' + re.escape(word) + '(?=[\s.?!])[^.?!]*[.?!]'
for i in text:
    match = re.findall(pattern, text)

for i in match:
    print(i.strip(' '))