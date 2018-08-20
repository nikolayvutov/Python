n = int(input())

s = sorted(dict())

for i in range(n):
    line = input().split(' ')
    continent, country, city = line[0], line[1], line[2]
    if line[0] in s:
        if line[1] in line[0]:
            s[line[0]][line[1]].append(line[2])
        else:
            s[line[0]][line[1]] = line[2]
    else:
        s[line[0]] = {
            line[1]: [line[2]]
        }
for key, value in s:
    print('{} -> {}'.format(key, value))