# How to convert a number from a Decimal to Binary using recursion?

def binary(number):
    assert int(number) == number, 'The number must be integer'
    if number == 0:
        return str(number % 2)
    return str(binary(int(number/2))) + str(number % 2)

print(binary(-12))
