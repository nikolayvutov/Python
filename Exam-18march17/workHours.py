neededHours = int(input())
workers = int(input())
workDays = int(input())


hours = workDays * workers * 8
left = hours - neededHours

if hours > neededHours:
    print('{0} hours left'.format(left))
else:
    print('{0} overtime\nPenalties: {1}'.format(abs(left), abs(left*workDays)))