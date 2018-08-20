hour = int(input())
min = int(input())

min = min + 15

if min >= 60:
    min = min - 60
    hour = hour + 1

if hour >23:
    hour = hour - 24
elif min >= 60:
    print(str(hour) + ":" + str(min))

if min < 10:
    print(str(hour) + ":0" + str(min))
else:
    print(str(hour) + ":" + str(min))


