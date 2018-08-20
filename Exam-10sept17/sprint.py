length = int(input())
people_number = int(input())
avg_laps = int(input())
lap_length = int(input())
route_capacity = int(input())
money_km =float(input())

total_runners = route_capacity * length

if total_runners < people_number:
    people_number = total_runners


total_km = (people_number * avg_laps * lap_length) / 1000
money = money_km * total_km

print('Money raised: {:.2f}'.format(money))