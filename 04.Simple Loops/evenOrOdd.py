n = int(input())

even = 0
odd = 0

for i in range(n):
    element = int(input())
    if i % 2 == 0:
        even += element
    else:
        odd += element

sum = even - odd

if even == odd:
    print('Yes')
    print('Sum = ' + str(odd))
else:
    print('No')
    print('Diff = '+ str(abs(sum)))