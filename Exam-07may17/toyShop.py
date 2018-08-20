tripPrice = float(input())
countPuzzels = int(input())
countBarbies = int(input())
countTedyBears = int(input())
countMinions = int(input())
countCars = int(input())

puzzels = countPuzzels * 2.60
barbies = countBarbies * 3
tedyBears = countTedyBears * 4.10
minions = countMinions * 8.20
cars = countCars * 2

sum = puzzels + barbies + tedyBears + minions + cars

countAll = countPuzzels + countBarbies + countTedyBears + countMinions + countCars

discount = 0

if countAll >= 50:
    discount = sum * 0.25

rent = (sum - discount)* 0.10

allSum = (sum - discount) - rent

if allSum >= tripPrice:
    print('Yes! {0:.2f} lv left.'.format(allSum - tripPrice))
else:
    print('Not enough money! {0:.2f} lv needed.'.format(abs(allSum-tripPrice)))