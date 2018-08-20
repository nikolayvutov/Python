examHours = int(input())
examMin = int(input())
studentHours = int(input())
studentMin = int(input())

examTime = examHours * 60 + examMin
studintTime = studentHours * 60 + studentMin
timeDiff = examTime - studintTime

if timeDiff < -30:
    print("Early")
elif timeDiff <= 0:
    print("On time")
else:
    print("Late")

if timeDiff > 0 or timeDiff < 0:
    hours = abs(timeDiff / 60)
    min = abs(timeDiff % 60)
    if hours > 0:
        if min < 10:
            print(str(hours) + ":0" + str(min))
        else:
            print(str(hours) + ":" + str(min))
    else:
        print(str(min) + " minutes")
    if timeDiff < 0:
        print(" before the start")
    else:
        print(" after the start")

print(timeDiff)