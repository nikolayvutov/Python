def greater_of_values(form, first, second):
    if form == 'int':

        Max = max(first, second)
        print(Max)
    elif form == 'char':

        Max = max(first, second)
        print(Max)
    elif form == 'string':

        Max = max(len(first), len(second))
        print(Max)

form = input()
first = input()
second = input()
greater_of_values(Max)
