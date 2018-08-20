products = list()
pc = {}

#n = input()

# while n != 'PC':
#     n = n.split(' ')
#     products.append(n[0])
#
#     n = input()
#
# print(products)
#
new = ''

line = input()
while line != 'END':
    line = line.split(' ')
    name, prod = line[1], line[2]
    if line[0] == 'ADDPC':
        if name not in pc:
            pc = [name]
    if line[0] == 'ADDPRODUCT':
        if line[1] in pc:
            pc[line[1]] = line[2], prod

        else:
            pc[line[1]] = line[2]
    # if line[0] == 'REMOVEPRODUCT':


    print(pc)
    line = input()
