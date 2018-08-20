season = input().lower()
monthKM = float(input())

sum = 0
if monthKM <= 5000:
    if season == 'spring' or season == 'autumn':
        sum = monthKM * 0.75
    elif season == 'summer':
        sum = monthKM * 0.90
    elif season == 'winter':
        sum = monthKM * 1.05
elif 5000 < monthKM <= 10000:
    if season == 'spring' or season == 'autumn':
        sum = monthKM * 0.95
    elif season == 'summer':
        sum = monthKM * 1.10
    elif season == 'winter':
        sum = monthKM * 1.25
else:
    sum = monthKM * 1.45

all = sum * 4
allSum = all - (all * 10 / 100)

print('%.2f' % allSum)
