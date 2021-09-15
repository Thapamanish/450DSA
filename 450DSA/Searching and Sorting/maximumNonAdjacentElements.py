#Question: Maximum Sum Non Adjacent Elements

# Time complexity: O(n)
                  
# Auxiliary Space: O(1)

# intution : use greedy approach of including and excluding


def solve(arr):
    n = len(arr)
    inc = arr[0]
    exc = 0

    for i in range(1, n):
        newInc = arr[i] + exc
        newExc = max(inc, exc)
        
        inc = newInc
        exc = newExc


    return max(inc, exc)
                



arr = [1,2,3]
print(solve(arr))