import math

hours = int(input())
days = int(input())
employees = int(input())

intern = days * 10 / 100
workDays = days - intern
hour = workDays * 8

workers = employees * (2 * days)
allHours = hour + workers

time = allHours - hours

if time >= 0:
    print("Yes!{0} hours left.".format(math.floor(time)))
else:
    print("Not enough time!{0} hours needed.".format(abs(math.floor(time))))
