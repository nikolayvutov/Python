n = [int(i) for i in input().split(' ')]
n.reverse()

for i in n:
    n[i] = str(n[i])
    print(i, end=' ')