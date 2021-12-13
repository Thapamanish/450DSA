# Question: find the pivot element in sorted and rotated array

# Time complexity: O(logn)
                  
# Auxiliary Space: O(2)

# intution : use property of binary search


def solve(arr):
    n = len(arr)
    if n == 1:
        return arr[0]
    low = 0
    high = n - 1
    while low < high:
        mid = low + (high - low) // 2
        if arr[mid] < arr[high]:
            high = mid
        else:
            low = mid + 1

    return arr[low]


arr = [30, 40, 50, 10, 20]
print(solve(arr))