nums = [float(i) for i in input().split(' ')]
n = float(input())
result = 0
list = []

for i in range(len(nums)):
    result = nums[i] * n
    list += [result]

for i in list:
    print(i, end=' ')