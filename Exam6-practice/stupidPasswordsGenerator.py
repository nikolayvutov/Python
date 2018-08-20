n = int(input())
l = int(input())

for i in range(1, n+1):

    for j in range(1, n+1):

        for k in range(97, 97 + l):

            for z in range(97, 97 + l):

                for m in range(1, n+1):

                    if m > i and m > j:
                        print("{0}{1}{2}{3}{4}".format(i, j, chr(k),chr(z), m), end=' ')