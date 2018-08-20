x = float(input())
y = float(input())
h = float(input())

walls = x * y
window = 1.5 * 1.5
door = 1.2 * 2

allWalls = (2 * walls) - 2 * window
backWall = x * x
frontAndBack = (2 * backWall) - door
wallsArea = frontAndBack + allWalls
greenPaint = wallsArea / 3.4

roofSides = 2* (x * y)
roofFrontBack = 2 * (x * h / 2)
roofArea = roofSides + roofFrontBack
redPaint = roofArea / 4.3

print('%.2f' %greenPaint)
print('%.2f' %redPaint)
