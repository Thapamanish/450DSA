def countBits(n):
    if n == 0:
        return 0

    return 1 + countBits(n & (n-1))


def flipCount(a, b):
    return countBits(a ^ b)


a = 20
b = 25
print(flipCount(a, b))