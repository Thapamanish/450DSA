# Time complexity: O(logN)
# Space complexity: O(1)

def isPower2(n):
    if n == 0:
        return True


    while n > 1 and n & 1 == 0:
        n = n >> 1

    return True if n == 1 else False


# Time complexity : O(1)
# Space complexity : O(1)

# def isPowerofTwo(n):
#     if n == 0:
#         return False
    
#     return n & (n - 1) == 0



n = 23
print(isPower2(n))