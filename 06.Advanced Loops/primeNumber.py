n = int(input())

prime = True
i = 2
if n < 2:
    print('Not Prime')
else:
    while i*i <= n:
        if n % i == 0:
            prime = False
            print('Not Prime')
            break
        i += 1
    else:
        print('Prime')


