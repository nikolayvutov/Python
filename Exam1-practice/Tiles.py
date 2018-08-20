import math

n = float(input())
w = float(input())
l = float(input())
m = float(input())
o = float(input())

place = n * n
tile = w * l
bench = m * o

answer = (place - bench) /tile
time = answer * 0.2

print("%.2f" % answer)
print("%.2f" % time)