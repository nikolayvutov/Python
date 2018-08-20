n = int(input())
m = int(input())
controlNumber = int(input())

sum1 = 0
sum2 = 0
sum = 0
allSum = 0
checkControl = False

for sum1 in range(1, n+1):
    for sum2 in range(m, 1, -1):
        sum += 1
        allSum = sum1 * 2 + sum2 + 3

        if allSum >= controlNumber:
            checkControl = True
            break
    if checkControl:
        break
print('{0} moves'.format(sum))

if True:
    print('Score: {0} >= {1}'.format(allSum, controlNumber))
