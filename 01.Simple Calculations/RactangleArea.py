x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())

width = max(x1, x2) - min(x1, x2)
height = max(y1, y2) - min(y1, y2)
print(width * height)
print(2 * (width + height))