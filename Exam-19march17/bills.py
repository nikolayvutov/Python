months = int(input())

water = 20
net = 15
others = 0
allElectricity = 0

for i in range(months):
    electricity = float(input())
    all = electricity + water + net
    others += all + (all * 20 / 100)
    allElectricity += electricity

allWater = months * water
allNet = months * net

average = (allElectricity + allWater + allNet + others) / months

print('Electricity: %.2f lv' %allElectricity)
print('Water: %.2f lv' %allWater)
print('Internet: %.2f lv' %allNet)
print('Other: %.2f lv' %others)
print('Average: %.2f lv' %average)

