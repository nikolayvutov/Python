n = int(input())

hours = 0
min = 0

dayOff = n * 127
workDays = 365 - n
minutes = workDays * 63
difference = 30000 - (minutes + dayOff)

if difference < 0:
    print("Tom will run away")
    if abs(difference) > 59:
        hours = abs(difference) // 60
        min = abs(difference) % 60
        print(str(hours) + " hours and " + str(min) + " minutes more for play")
    elif abs(difference) < 59:
        min = abs(difference)
        print("0 hours and " + str(min) + " minutes more for play")
else:
    print("Tom sleeps well")
    if abs(difference) > 59:
        hours = abs(difference) // 60
        min = abs(difference) % 60
        print(str(hours) + " hours and " + str(min) + " minutes less for play")
    elif abs(difference) < 59:
        min = abs(difference)
        print("0 hours and " + str(min) + " minutes less for play")