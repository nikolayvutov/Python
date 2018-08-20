def rev(list):
    for i in range(len(list) // 2):
        curr = list[i]
        list[i] = list[-i - 1]
        list[-i -1] = curr

nums = [item for item in input().split(' ')]

rev(nums)
print(' '.join(nums))