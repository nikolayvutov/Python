import math

n = int(input())
rowCount = math.ceil(n /2 )
stars = '*'

for row in range(rowCount):
    if n % 2 == 1:
        for i in range(n // 2 - row):
            print('-', end='')
        print(stars, end='')
        stars += '**'
        for i in range(n // 2 - row):
            print('-', end='')
    else:
        stars += '*'
        for i in range(n // 2 - row- 1):
            print('-', end='')
        print(stars, end='')
        stars += '*'
        for i in range(n // 2 - row- 1):
            print('-', end='')
    print()
for i in range(n // 2):
    print('|', end='')
    for j in range(n-2):
        print('*', end='')
    print('|')