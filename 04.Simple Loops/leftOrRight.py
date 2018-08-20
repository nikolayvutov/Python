n = int(input())

leftSum = 0
rightSum = 0

for i in range(n):
    leftSum = leftSum + int(input())
for i in range(n):
    rightSum = rightSum + int(input())

if leftSum == rightSum:
    print('Yes, sum = ' + str(leftSum))
else:
    print('No, diff = ' + str(abs(rightSum - leftSum)))