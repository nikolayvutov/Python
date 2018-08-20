import math

length = int(input())
width = float(input())

length *= 100

if math.floor(width) == math.ceil(width):
    try:
        if length % int(width) == 0:
            print('%.2f' %(width * length))
        else:
            print('{0:.2f}%'.format(length / width * 100))
    except ZeroDivisionError:
        print('%.2f' % (width * length))
else:
    print('%.2f' %(width * length))