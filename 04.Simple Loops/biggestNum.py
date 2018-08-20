n = int(input())

max = -1000000

for i in range(n):
    num = int(input())
    if num > max:
        max = num
print(str(max))