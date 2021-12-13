# Question : program to segregate 0, 1, 2 without any algorithm

# Time Complexity: O(n)

# Space Complexity : O(1)

# Intution : use three pointer technique 


def solve(arr, n):
    low = 0
    mid = 0
    high = n - 1


    while mid <= high:
        if arr[mid] == 0:
            arr[mid], arr[low] = arr[low], arr[mid]
            low += 1
            mid += 1
        elif arr[mid] == 1:
            mid += 1

        else:
            arr[mid], arr[high] = arr[high], arr[mid]
            high -= 1

    return arr



arr = [1,2,1,0,1,2,0]
print(solve(arr, len(arr)))