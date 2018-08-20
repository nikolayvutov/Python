countCups = int(input())
countWorkers = int(input())
workDays = int(input())

hours = countWorkers * workDays * 8
cups = hours // 5
cupsMoney = abs(countCups - cups) * 4.20

if countCups > cups:
    print('Losses: {0:.2f}'.format(cupsMoney))
else:
    print('{0:.2f} extra money'.format(cupsMoney))