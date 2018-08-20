firstNumber = int(input())
secondNumber = int(input())
operator = input()


if operator == '+':
    result = firstNumber + secondNumber
    if result % 2 == 0:
        print('{0} + {1} = {2} - even'.format(firstNumber , secondNumber, result))
    else:
        print('{0} + {1} = {2} - odd'.format(firstNumber, secondNumber, result))
elif operator == '-':
    result = firstNumber - secondNumber
    if result % 2 == 0:
        print('{0} - {1} = {2} - even'.format(firstNumber , secondNumber, result))
    else:
        print('{0} - {1} = {2} - odd'.format(firstNumber, secondNumber, result))
elif operator == '*':
    result = firstNumber * secondNumber
    if result % 2 == 0:
        print('{0} * {1} = {2} - even'.format(firstNumber , secondNumber, result))
    else:
        print('{0} * {1} = {2} - odd'.format(firstNumber, secondNumber, result))
elif secondNumber == 0:
    print('Cannot divide {0} by zero'.format(firstNumber))
elif operator == '/':
    result = firstNumber / secondNumber
    print('{0} / {1} = {2:.2f}'.format(firstNumber , secondNumber, result))
elif operator == '%':
    result =  firstNumber % secondNumber
    print('{0} % {1} = {2}'.format(firstNumber, secondNumber, result))