width = float(input())
hight = float(input())

bothSides = width * (width / 2) * 2
backSide = (width / 2) * (width / 2)
triangle = (width / 2) * (hight - width / 2) / 2
backSideResult = backSide + triangle

enter = (width / 5) * (width / 5)
front = backSideResult - enter
all = front + backSideResult + bothSides

green = all / 3
roof = width * (width / 2) * 2
red = bothSides / 5

print('%.2f' % green)
print('%.2f' % red)
