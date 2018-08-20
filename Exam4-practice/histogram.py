n = int(input())

p1 = 0
p2 = 0
p3 = 0
p4 = 0
p5 = 0

for i in range(n):
    num = int(input())

    if num < 200:
        p1 += 1
    elif num < 400:
        p2 += 1
    elif num < 600:
        p3 += 1
    elif num < 800:
        p4 += 1
    elif num >= 800:
        p5 += 1

p1Percentage = p1 * 100 / n
p2Percentage = p2 * 100 / n
p3Percentage = p3 * 100 / n
p4Percentage = p4 * 100 / n
p5Percentage = p5 * 100 / n

print("{0:.2f}%".format(p1Percentage))
print("{0:.2f}%".format(p2Percentage))
print("{0:.2f}%".format(p3Percentage))
print("{0:.2f}%".format(p4Percentage))
print("{0:.2f}%".format(p5Percentage))
