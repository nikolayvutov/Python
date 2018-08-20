unique = []
s = {}

while True:
    n = input().split(' = ')
    if n[0] != 'end':
        if n[0] in s:
            if n[1] != int(n[1]):
                value = n[1]
            # Да завъртя стойностите
            else:
                s[n[0]].append(n[1])
        else:
            s[n[0]] = [n[1]]
            unique.append(n)
    else:
        break

for key in unique:
    if key[1] == key[0]:

    print('{} === {}'.format(key[0], key[1]))
