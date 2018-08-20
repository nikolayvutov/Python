import math

figure = input()

if figure == "square":
    a = float(input())
    area = a * a
    print("{0:.3F}".format(area))
elif figure == "rectangle":
    a = float(input())
    b = float(input())
    area = a * b
    print("{0:.3F}".format(area))
elif figure == "circle":
    r = float(input())
    area = (r ** 2) * math.pi
    print("{0:.3F}".format(area))
elif figure == "triangle":
    a = float(input())
    h = float(input())
    area = (a * h) / 2
    print('%.3f' % area)