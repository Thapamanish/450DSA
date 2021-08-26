# Time complexity : O(N)
# Space complexity : O(1)

def solve(arr, n):
    low = 0
    high = n - 1
    while low <= high:
        if arr[low] < 0 and arr[high] > 0:
            low += 1
            high -= 1

        elif arr[low] > 0 and arr[high] < 0:
            arr[low], arr[high] = arr[high], arr[low]
            high -= 1

        elif arr[low] < 0 and arr[high] < 0:
            low += 1

        else:
            high -= 1



    return arr



arr=[-12, 11, -13, -5,6, -7, 5, -3, 11]
print(solve(arr, len(arr)))
