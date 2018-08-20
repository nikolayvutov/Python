nums = [int(i) for i in input().split(' ')]

count = 0
nums = nums[1:len(nums):2]
li = []

for i in nums:
    if i % 2 == 1:
        li += [i]
        res = li.index(i)

for i in li:
    print('Index {0} -> {1}'.format(li.index(i), i))
