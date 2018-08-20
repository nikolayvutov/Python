n = int(input())

f0 = 1
f1 = 1
for i in range(n-1):
    fNext = f0 + f1
    f0 = f1
    f1 = fNext
print(fNext)