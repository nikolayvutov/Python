import math

year = input()
p = int(input())
h = int(input())

weekends = (48 - h) * 3 / 4
hollydays = p * 2 / 3
all = weekends + h + hollydays

if year == 'leap':
    bonus = all * 15 / 100
    print(math.floor(all + bonus))
else:
    print(math.floor(all))