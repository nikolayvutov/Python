import math

area = int(input())
y = float(input())
litters = int(input())
workers = int(input())

grapes = area * y
wines = (grapes / 2.5) * 40 / 100
n = wines - litters

if n < 0:
    print('It will be a tough winter! More {0} liters wine needed.'.format(abs(round(n))))
elif n >= 0:
    p = n / workers
    print('Good harvest this year! Total wine: {0} liters.'.format(math.floor(wines)))
    print('{0} liters left -> {1} liters per person.'.format(round(n), round(p)))