n = int(input())

sum = 0
Max = int(input())
sum += Max

for i in range(1, n):
    curr = int(input())
    sum += curr
    Max = max(Max, curr)
if Max == sum - Max:
    print('Yes\nSum = {0}'.format(Max))
else:
    print('No\nDiff = {0}'.format(abs(Max - (sum - Max))))