city = input().lower()
n = float(input())

result = -1

if city == 'sofia':
    if n >= 0 and n <= 500:
        result = n * 5 / 100
    elif n > 500 and n <= 1000:
        result = n * 7 / 100
    elif n > 1000 and n <=10000:
        result = n * 8 / 100
    elif n > 10000:
        result = n * 12 / 100
elif city == 'varna':
    if n >= 0 and n <= 500:
        result = n * 4.5 / 100
    elif n > 500 and n <= 1000:
        result = n * 7.5 / 100
    elif n > 1000 and n <=10000:
        result = n * 10 / 100
    elif n > 10000:
        result = n * 13 / 100
elif city == 'plovdiv':
    if n >= 0 and n <= 500:
        result = n * 5.5 / 100
    elif n > 500 and n <= 1000:
        result = n * 8 / 100
    elif n > 1000 and n <=10000:
        result = n * 12 / 100
    elif n > 10000:
        result = n * 14.5 / 100

if result >= 0:
    print("%.2f" %result)
else:
    print('error')