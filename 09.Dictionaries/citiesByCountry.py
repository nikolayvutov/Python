n = int(input())

continents = {}

for i in range(n):
    str = input().split(' ')
    if str[0] in continents:
        if str[1] in continents[str[0]]:
            continents[str[0]][str[1]].append(str[2])
        else:
            continents[str[0]][str[1]] = [str[2]]
    else:
        continents[str[0]] = {
            str[1]: [str[2]]
        }

for i in continents:
    print('{}'.format(i))
    for task in continents[i]:
        print('\t {} -> '.format(task), end='')
        print()
