age = int(input())
price = float(input())
toyPrice = int(input())

money = 0
toy = 0
steels = 0

for i in range(age + 1):
    if i % 2 == 0:
        money += i * 10 / 2
        steels += 1
    else:
        toy += 1
brother = age // 2
toyMoney = toy * toyPrice
sum = (money + toyMoney) - brother
all = sum - price

if sum >= price:
    print("Yes! {0:.2f}".format(all))
else:
    print("No! {0:.2f}".format(abs(all)))

