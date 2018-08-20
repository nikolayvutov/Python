import math

n = int(input())

for row in range(n):
    if row == 0 or row == n-1:
        for col in range(2*n):
            print('*', end='')
        for col in range(n):
            print(' ', end='')
        for col in range(2*n):
            print('*', end='')
    elif math.ceil (n /2)-1 == row:
        print('*', end='')
        for j in range(2*n-2):
            print('/', end='')
        print('*', end='')
        for col in range(n):
            print('|', end='')
        print('*', end='')
        for j in range(2*n-2):
            print('/', end='')
        print('*', end='')
    else:
        print('*', end='')
        for j in range(2 * n - 2):
            print('/', end='')
        print('*', end='')
        for col in range(n):
            print(' ', end='')
        print('*', end='')
        for j in range(2 * n - 2):
            print('/', end='')
        print('*', end='')
    print()