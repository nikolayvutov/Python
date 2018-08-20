type = input().lower()
r = int(input())
c = int(input())

area = r * c
price = -1

if type == 'premiere':
    price = area * 12
elif type == 'normal':
    price = area * 7.50
elif type == 'discount':
    price = area * 5

print("{0:.2f} leva".format(price))

