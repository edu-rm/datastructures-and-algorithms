# How to find GCD (Greatest Common Divisor) of two numbers using recursion?

# Using euclidian algorithm

def gcd(a, b):
    assert int(a) == a and int(b) == b, 'The numbers must be integers'
    if a < 0:
        a = a * -1
    if b < 0:
        b = b * -1
    if a == 0:
        return b
    if b == 0:
        return a

    return gcd(b, int(a % b))


print(gcd(-192, 270))
