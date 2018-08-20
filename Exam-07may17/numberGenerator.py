m = int(input())
n = int(input())
l = int(input())
specialNumber = int(input())
controlNumber = int(input())

reached = 0

for i in range(m, 0, -1):
    for j in range(n, 0, -1):
        for k in range(l, 0, -1):
            number = (i * 100) + (j * 10) + k
            reached = 0
            if number % 3 == 0:
                specialNumber += 5
            elif number % 10 == 5:
                specialNumber -= 2
            elif number % 2 == 0:
                specialNumber *= 2
            if specialNumber >= controlNumber:
                reached = True
                break



if reached:
    print('Yes! Control number was reached! Current special number is {0}.'
      .format(specialNumber % 100))

else:
    print('No! {0} is the last reached special number.'
      .format(specialNumber))
