product = input().lower()
city = input().lower()
n = float(input())

if city == 'sofia':
    if product =='coffee':
        result = n * 0.50
    elif product == 'water':
        result = n * 0.80
    elif product == 'beer':
        result = n * 1.20
    elif product == 'sweets':
        result = n * 1.45
    elif product == 'peanuts':
        result = n * 1.60
elif city == 'plovdiv':
    if product =='coffee':
        result = n * 0.40
    elif product == 'water':
        result = n * 0.70
    elif product == 'beer':
        result = n * 1.15
    elif product == 'sweets':
        result = n * 1.30
    elif product == 'peanuts':
        result = n * 1.50
elif city == 'varna':
    if product =='coffee':
        result = n * 0.45
    elif product == 'water':
        result= n * 0.70
    elif product == 'beer':
        result = n * 1.10
    elif product == 'sweets':
        result = n * 1.35
    elif product == 'peanuts':
        result = n * 1.55

print("{0:.2f}".format(result))