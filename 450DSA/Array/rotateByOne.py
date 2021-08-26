# Time Complexity : O(n)
# Space Complexity : O(1)


def rotate( arr, n):
    i = 0
    j = n -1 
    while i <= j:
        arr[i], arr[j] = arr[j], arr[i]
        i += 1
    return arr

print(rotate([1,2,3,4,5], 5))