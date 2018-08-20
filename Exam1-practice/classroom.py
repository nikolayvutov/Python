w = float(input())
h = float(input())

long = (w * 100) // 120
width = ((h * 100) - 100) // 70

seats = long * width -3
print("%.2f" % seats)

