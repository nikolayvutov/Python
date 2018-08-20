nums = [int(i) for i in input().split(' ')]

result = 0
li = []
for i in nums:
    if i >= 0:
        li += [i]
    else:
        continue
if li == []:
    print('empty')
else:
    li.reverse()

    for i in li:
        print(i, end=' ')