# Time complexity: O(N)
# Space complexity: O(N)

#intution : Prefix Sum

def solve(arr):
    isZero = set()
    pSum = 0
    for i in range(len(arr)):
        pSum += arr[i]

        if pSum == 0 or pSum in isZero:
            return True

        isZero.add(pSum)

    return False



arr = [4, 2, -3, 1, 6]
print(solve(arr))