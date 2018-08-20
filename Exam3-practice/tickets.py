money = float(input())
category = input().lower()
people = int(input())

vip = 499.99
normal = 249.99

if 1 <= people <= 4:
    ticketMoney = money - (money * 75 / 100)

elif 5 <= people <= 9:
    ticketMoney = money - (money * 60 / 100)

elif 10 <= people <= 24:
    ticketMoney = money - (money * 50 / 100)

elif 25 <= people <= 49:
    ticketMoney = money - (money * 40 / 100)

elif people >= 50:
    ticketMoney = money - (money * 25 / 100)

if category == 'normal':
    tickets = people * normal
    moneyLeft = ticketMoney - tickets
    if moneyLeft >= 0:
        print('Yes! You have %.2f leva left.' %moneyLeft)
    else:
        print('Not enough money! You need %.2f leva.' %abs(moneyLeft))
elif category == 'vip':
    tickets = people * vip
    moneyLeft = ticketMoney - tickets
    if moneyLeft >= 0:
        print('Yes! You have %.2f leva left.' %moneyLeft)
    else:
        print('Not enough money! You need %.2f leva.' %abs(moneyLeft))
