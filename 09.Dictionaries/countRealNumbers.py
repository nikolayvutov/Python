nums = [float(i) for i in input().split(' ')]

count = {}

for i in nums:
    if i in count:
        count[i] += 1
    else:
        count[i] = 1

for num in sorted(count):
    print('{} -> {}'.format(num if num != int(num) else int(num), count[num]))