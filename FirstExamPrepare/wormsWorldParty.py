line = input()

teams = dict()

all_members = set()

while line != 'quit':
    line = line.split('->')
    name, team, score = line[0], line[1], int(line[2])
    if not(name in all_members):
        if team in teams:
            teams[team][name] = score
        else:
            teams[team] = {name: score}
        all_members.add(name)
    line = input()

count = 1

for team in reversed(sorted(teams.keys())):
    print('{0}. Team:{1}- {2}'.format(count, team, sum(teams[team].values())))
    for member in reversed(sorted(teams[team].items(), key=lambda x: (x[1]))):
        print('   {0}: {1}'.format(member[0], member[1]))
    count += 1