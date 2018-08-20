n = int(input())

num = 1
for i in range(1, n+1):
    for j in range(i):
        if i > 0:
            print(' ', end='')
        print(num, end='')
        num += 1
        if num > n:
            break
    print()
    if num > n:
        break