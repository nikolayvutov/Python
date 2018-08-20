n = int(input())

for i in range(1, 10):
    if n % i != 0:
        continue
    for j in range(1, 10):
        if n % j != 0:
            continue
        for k in range(1, 10):
            if n % k != 0:
                continue
            for m in range(1, 10):
                if n % m != 0:
                    continue
                for o in range(1, 10):
                    if n % o != 0:
                        continue
                    for p in range(1, 10):
                        if n % i != 0:
                            continue
                        if (i * j * k * m * o * p == n):
                            print("{0}{1}{2}{3}{4}{5}".format(i, j, k, m, o, p), end=' ')