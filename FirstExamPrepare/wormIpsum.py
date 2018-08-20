import re

sentance = input()

while sentance != 'Worm Ipsum':
    if len(re.findall('\.', sentance)) == 1:
        output = []
        for word in sentance[:-1].split(' '):
            dict = {}
            for c in word:
                if c in dict:
                    dict[c] += 1
                else:
                    dict[c] = 1
            most_char = list(dict.keys())[0]
            for c in dict.keys():
                if dict[c] > dict[most_char]:
                    most_char = c
            if dict[most_char] > 1:
                output.append(most_char * len(word))
            else:
                output.append(word)

        print(' '.join(output) + '.')

    sentance = input()