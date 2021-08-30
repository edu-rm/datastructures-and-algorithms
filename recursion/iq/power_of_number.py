# How to calculate the power of a number using recursion ?

def powerOfNumber(number, exp):
    assert int(exp) == exp and exp >= 0, 'The exponent must be positive and integer'
    if exp == 0:
        return 1
    else:
        return number * powerOfNumber(number, exp-1)

print(powerOfNumber(3, 3))