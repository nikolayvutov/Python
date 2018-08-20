n = int(input())

divideBy2 = 0
divideBy3 = 0
divideBy4 = 0

for i in range(n):
    number = int(input())

    if number % 2 == 0:
        divideBy2 += 1
    if number % 3 == 0:
        divideBy3 += 1
    if number % 4 == 0:
        divideBy4 += 1

print("{0:.2f}%".format((divideBy2 / n) * 100))
print("{0:.2f}%".format((divideBy3 / n) * 100))
print("{0:.2f}%".format((divideBy4 / n) * 100))