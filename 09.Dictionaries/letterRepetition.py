n = input()

count = {}

for i in n:
    if i in count:
        count[i] += 1
    else:
        count[i] = 1

for i in count:
    print('{} -> {}'.format(i, count[i]))