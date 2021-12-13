# Time complexity : O(n)
# Space complexity : O(1)



def isPowerOf2(n):
    if n == 0:
        return False

    return not n & (n - 1)



def setBitPos(n):
    if not isPowerOf2(n):
        return -1


    count = 0
    while n:
        n >>= 1
        count += 1

    return count



n = 2
print(setBitPos(n))