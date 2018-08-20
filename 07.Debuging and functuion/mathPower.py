def reise_to_power(number, power):
    result = 1;
    for i in range(power):
        result *= number
    return result

number = float(input())
power = int(input())
result = reise_to_power(number, power)
print(result if result != int(result) else int(result))