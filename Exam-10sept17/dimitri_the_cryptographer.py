n = input()

first_table = {}
second_table = {}
third_table = {}



while n != 'STOP':
    old = n[0]
    new = n[5]
    first_table[old] = new

    n = input()

line = input()

for i in line:
    if i in first_table:
        line.replace(i, first_table[i])

        print(first_table)