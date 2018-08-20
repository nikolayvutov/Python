magic = int(input())

for num in range(10000, 100000):
    a = num // 10000
    b = num // 1000 % 10
    c = num // 100 % 10
    d = num // 10 % 10
    e = num // 1 % 10
    try:
        f = magic / a / b / c / d / e // 1
        if (a * b * c * d * e * f == magic):
            print(num)
    except:
        continue