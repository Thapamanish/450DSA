# Time complexity: O(n)
                  
# Auxiliary Space: O(1)

# intution : use the formula (arr[i] - x) // k to increment the i

def search(arr, n, x, k):
    i = 0
    for i in range(n):
        if arr[i] == x:
            return i
            
        i += max(1, abs(arr[i] - x) // k)
        
    return -1



arr = [4, 5, 6, 7, 6]
x = 6
k = 1
print(search(arr, len(arr), x, k))