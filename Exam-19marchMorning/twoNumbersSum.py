start = int(input())
end = int(input())
magicNumber = int(input())

count = 0
sum = start + end

for i in range(start, end-1,-1):
    for j in range(start, end-1 ,-1):

        sum = i + j
        count +=1
        if i + j == magicNumber:
            print('Combination N:{0} ({1} + {2} = {3})'.format(count, i, j, magicNumber))
            break
    if i + j == magicNumber:
        break
else:
    print('{0} combinations - neither equals {1}'.format(count, magicNumber))

