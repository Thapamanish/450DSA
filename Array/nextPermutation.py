# Question : program to find the next permutation

# Time Complexity: O(n)

# Space Complexity : O(1)

# Intution : dictionary order 

def solve(arr):
    n = len(arr)
    k = n - 2
    while k >= 0:
        if arr[k] < arr[k + 1]:
            break
        k -= 1
    
    if k < 0 :
        arr = arr[::-1]
    else:
        for l in range(n -1 , k, -1):
            if arr[l] > arr[k]:
                break

        arr[l], arr[k] = arr[k], arr[l]
        arr[k + 1:] = reversed(arr[k + 1:])

    return arr



arr = [1,3,2]
print(solve(arr))
