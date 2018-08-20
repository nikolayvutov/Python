nums =[int(i) for i in input().split(' ')]

count = 0
for item in nums:
    if item % 2 == 1:
        count += 1
print(count)