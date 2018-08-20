n = int(input())

for row in range(n):
    for col in range(n-row-1):
        print(' ', end='')
    print('*', end='')
    for col in range(row):
        print(' *', end='')
    print()
for row in range(n, 0,-1):
    for col in range(n-row):
        print(' ', end='')
    for col in range(row-1):
        print(' *', end='')
    print()
