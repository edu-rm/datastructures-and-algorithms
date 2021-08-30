# How to find the sum of digits of a positive integer number using recursion?
# 123 = 6

def sumOfDigits(number, counter):
    assert str(int(number)) == number and int(number) >= 0, 'The number must be a number and positive'
    if counter <= len(number) - 1:
        return int(number[counter]) + sumOfDigits(number, counter + 1)
    else:
        return 0


def sumOfDigitsDivisionByTen(number):
    assert int(number) == number and number >= 0, 'The number must be integer and positive'
    if number >= 10:
        return (number % 10) + sumOfDigitsDivisionByTen(int(number / 10))
    else:
        return number


# number = str(99999999)

# print(sumOfDigits(number, 0))
print(sumOfDigitsDivisionByTen(99))
