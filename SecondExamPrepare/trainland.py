inp = input()

trains = []

while inp != "It's Training Men!":
    inp = inp.split(' ')
    if inp[1] == '->' and len(inp) == 5:
        ex = False
        for i in range(len(trains)):
            name, wagons = trains[i]
            if name == inp[0]:
                ex = True
                wagons += [(inp[2], int(inp[4]))]
                trains[i] = (name, wagons)
                break

        if not ex:
            trains += [(inp[0], [(inp[2], int(inp[4]))])]

    elif inp[1] == '->' and len(inp) == 3:
        ind1 = -1
        ind2 = -1
        for i in range(len(trains)):
            name, wagons = trains[i]
            if name == inp[0]:
                ind1 = i
            if name == inp[2]:
                ind2 = i

        if ind1 == -1:
            t2n, t2w = trains[ind2]
            trains += (inp[0], t2w)
            trains[ind2] = [(t2n, [])]

        else:
            t1n, t1w = trains[ind1]
            t2n, t2w = trains[ind2]
            trains[ind1] = (t1n, t1w + t2w)



    else:
        for i in range(len(trains)):
            name, wagons = trains[i]
            if name == inp[0]:
                ind1 = i
            if name == inp[2]:
                ind2 = i

        if ind1 == -1:
            trains += [(inp[0], t2w)]
        else:
            t1n, t1w = trains[ind1]
            t2n, t2w = trains[ind2]
            trains[ind1] = (t1n, t2w)

    inp = input()

def func(x):
    sum = 0
    _, wagons = x
    for n, p in wagons:
        sum += p
    return -sum

def wf(x):
    n, v = x
    return -v

trains = sorted(trains, key=func)
for i in range(len(trains)):
    n, w = trains[i]
    w = sorted(w, key=wf)
    trains[i] = (n, w)

for i in trains:
    n, w = i
    if len(w) > 0:
        print("Train:", n)
        for j in w:
            n, p = j
            print("###{0} - {1}".format(n, p))
    else:
        break