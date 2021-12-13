# Question : program to rotate the array by one

# Time Complexity: O(n)

# Space Complexity : O(1)

# Intution : use two pointer technique but don't increament one pointer


def rotate( arr):
    n = len(arr)
    i = 0
    j = n - 1 
    while i <= j:
        arr[i], arr[j] = arr[j], arr[i]
        i += 1
    return arr

arr = [1,2,3,4,5]
print(rotate(arr))