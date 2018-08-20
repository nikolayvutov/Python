def insertion_sort(list):
    lastSorted = 0
    while lastSorted != len(list) - 1:
        currIndex = lastSorted
        while currIndex >= 0 and list[currIndex] > list[lastSorted + 1]:
            currIndex -= 1
        currElement = list[lastSorted + 1]
        list.pop(lastSorted + 1)
        list.insert(currIndex + 1, currElement)
        lastSorted += 1

nums = [int(item) for item in input().split(' ')]

insertion_sort(nums)

for i in range(len(nums)):
    nums[i] = str(nums[i])

print(' '.join(nums))