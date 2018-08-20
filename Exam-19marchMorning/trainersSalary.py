lectures = int(input())
budget = float(input())

jelev = 0
royal = 0
roli = 0
trofon = 0
sino = 0
others= 0

for i in range(lectures+1):
    name = input().capitalize()

    if name == 'Jelev':
        jelev += 1
    elif name == 'Royal':
        royal += 1
    elif name == 'Roli':
        roli += 1
    elif name == 'Trofon':
        trofon += 1
    elif name == 'Sino':
        sino += 1
    else:
        others += 1

salaryJelev = (budget / lectures) * jelev
salaryRoyal = (budget / lectures) * royal
salaryRoli = (budget / lectures) * roli
salaryTrofon = (budget / lectures) * trofon
salarySino = (budget / lectures) * sino
salaryOthers = (budget / lectures) * others

print('Jelev salary: {0:.2f} lv'.format(salaryJelev))
print('RoYaL salary: {0:.2f} lv'.format(salaryRoyal))
print('Roli salary: {0:.2f} lv'.format(salaryRoli))
print('Trofon salary: {0:.2f} lv'.format(salaryTrofon))
print('Sino salary: {0:.2f} lv'.format(salarySino))
print('Others salary: {0:.2f} lv'.format(salaryOthers))

