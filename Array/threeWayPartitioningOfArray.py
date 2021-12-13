# Time Complexity: O(N)
# Space Complexity: O(1)

# intution : Dutch National Flag based quick sort

def threeWayPartition(arr, n, lowVal, highVal):
    start = 0
    end = n - 1
    i = 0
 
    while i <= end:
 
        # If current element is smaller than
        # range, put it on next available smaller
        # position.
        if arr[i] < lowVal:
            arr[i], arr[start] = arr[start], arr[i]
            i += 1
            start += 1
 
        # If current element is greater than
        # range, put it on next available greater
        # position.
        elif arr[i] > highVal:
            arr[i], arr[end] = arr[end], arr[i]
            end -= 1
 
        else:
            i += 1
 

arr = [1, 14, 5, 20, 4, 2, 54,
       20, 87, 98, 3, 1, 32]
n = len(arr)

threeWayPartition(arr, n, 10, 20)

print("Modified array :", *arr)