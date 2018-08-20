n = int(input())

evenSum = 0
evenMax = -100000000000.0
evenMin = 100000000000.0
oddSum = 0
oddMax = -100000000000.0
oddMin = 100000000000.0

for i in range(1, n + 1):
    curr = float(input())

    if i % 2 == 0:
        evenSum += curr
        evenMax = max(evenMax, curr)
        evenMin = min(evenMin, curr)

    else:
        oddSum += curr
        oddMax = max(oddMax, curr)
        oddMin = min(oddMin, curr)
if oddMin == 100000000000.0:
    oddMin = 'no'
elif evenMin == 100000000000.0:
    evenMin = 'no'
elif oddMax == -100000000000.0:
    oddMax = 'no'
elif evenMax == -100000000000.0:
    evenMax = 'no'
else:
    evenMax = "{0:.1f}".format(evenMax)
    evenMin = "{0:.1f}".format(evenMin)
    oddMax = "{0:.1f}".format(oddMax)
    oddMin = "{0:.1f}".format(oddMin)

print("OddSum={0}, OddMin={1}, OddMax={2}, EvenSum={3}, EvenMin={4}, EvenMax={5}".
      format(oddSum, oddMin, oddMax, evenSum, evenMin, evenMax))