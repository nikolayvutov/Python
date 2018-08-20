def multiple_evens_and_odds(n):
    return sum_of_even(n) * sum_of_odd(n)

def sum_of_even(n):
    result = 0
    while n != 0:
        result += n % 10 if (n % 10) % 2 == 0 else 0
        n //= 10
    return result

print(multiple_evens_and_odds(abs(int(input()))))
def sum_of_odd(n):
    result = 0
    while n != 0:
        result += n % 10 if (n % 10) % 2 == 1 else 0
        n //= 10
    return result

