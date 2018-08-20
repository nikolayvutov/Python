number = int(input())

inRange = (number >= 100 and number <= 200) or number == 0
if not inRange:
    print('invalid')