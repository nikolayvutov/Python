n = 0
while True:
    try:
        n = int(input('Enter even number: '))
        if n % 2 == 0:
            break
        print('The number is not even.')
    except ValueError:
        print('Invalid number')
print('Even number entered:', n)