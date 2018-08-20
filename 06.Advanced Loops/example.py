import math
n = int(input())

for row in range(n):
    for col in range(n):
        if col < n - row:
            print(row + col + 1, end=' ')
        else:
            print(n - row + n - col - 1, end=' ')
    print()
