n = int(input())
m = input()

taxi = (n * 0.79) + 0.70
taxiNight = (n * 0.90) + 0.70
bus = n * 0.09
train = n * 0.06


if n < 20 and m == 'day':
    print(taxi)
elif n < 20 and m == 'night':
    print(taxiNight)
elif n >= 20 and n <= 99:
    print(bus)
elif n >= 100:
    print(train)

