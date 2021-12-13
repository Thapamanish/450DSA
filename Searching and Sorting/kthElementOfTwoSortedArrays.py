# Question: find the kth element in two sorted array

# Time complexity: O(log(min(m, n)))
                  
# Auxiliary Space: O(1)

# intution : use property of binary search


def solve(A, B, k):
    n = len(A)
    m = len(B)

    if m < n:
        return solve(B, A, k)

    start = max(0, k - m)
    end = min(k, n)

    while start <= end:
        leftASize = (start + end) // 2
        leftBSize = k - leftASize

        leftA = A[leftASize - 1] if (leftASize > 0) else float('-inf')
        leftB = B[leftBSize - 1] if (leftBSize > 0) else float('-inf')
        rightA = A[leftASize] if (leftASize < n) else float('inf')
        rightB = B[leftBSize] if (leftBSize < m) else float('inf')

        if leftA <= rightB and leftB <= rightA:
            return max(leftA, leftB)

        elif leftA > rightB:
            end = leftASize - 1


        else:
            starS = leftASize + 1




arr1 = [4, 6]
arr2 = [1,2,3,5]
k = 6
print(solve(arr1, arr2, k))