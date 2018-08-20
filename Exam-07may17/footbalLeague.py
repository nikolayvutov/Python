stadiumCapacity = int(input())
fansCount = int(input())

procentA = 0
procentB = 0
procentV = 0
procentG = 0

for i in range(fansCount):
    n = input().upper()
    if n == 'A':
        procentA += 1
    elif n == 'B':
        procentB += 1
    elif n == 'V':
        procentV += 1
    elif n == 'G':
        procentG += 1

a = (procentA / fansCount) * 100
b = (procentB / fansCount) * 100
v = (procentV / fansCount) * 100
g = (procentG / fansCount) * 100

sum = (fansCount / stadiumCapacity) * 100

print('{0:.2f}% \n{1:.2f}%\n{2:.2f}% \n{3:.2f}%\n{4:.2f}%'
      .format(a,b,v,g,sum))