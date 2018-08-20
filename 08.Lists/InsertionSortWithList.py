def insertion_sort(list):
    result = list[:1]
    list.pop(0)
    while len(list) != 0:
        currentIndex = len(result) - 1
        while currentIndex >= 0 and list[0] < result[currentIndex]:
            currentIndex -= 1
        result.insert(currentIndex + 1, list[0])
        list.pop(0)
    return result

nums = [int(item) for item in input().split(' ')]
nums = insertion_sort(nums)

for i in range(len(nums)):
    nums[i] = str(nums[i])
print(' '.join(nums))