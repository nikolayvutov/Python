a = float(input())
start = input()
end = input()

if start == "mm":
    a = a
elif start == "cm":
    a = a * 10
elif start == "m":
    a = a * 100 * 10
elif start == "mi":
    a = a * 10 * 100 / 0.000621371192
elif start == "in":
    a = a * 10 * 100 /39.3700787
elif start == "km":
    a = a * 1000000
elif start == "ft":
    a = a * 1000 / 3.2808399
elif start == "yd":
    a = a * 1000 / 1.0936133

if end == "mm":
    a = a
elif end == "cm":
    a = a / 10
elif end == "m":
    a = a / 10 / 100
elif end == "mi":
    a = a /10 /100 * 0.000621371192
elif end == "in":
    a = a / 10 /100 * 39.3700787
elif end == "km":
    a = a /10 /100 * 0.001
elif end == "ft":
    a = a /10 /100 * 3.2808399
elif end == "yd":
    a = a /10 /100 * 1.0936133

print(a, end)