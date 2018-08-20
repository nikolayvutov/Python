n = int(input())

min = 10000000

for i in range(n):
    num = int(input())
    if num < min:
        min = num
print(str(min))