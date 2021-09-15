# Time complexity: O(n)
                  
# Auxiliary Space: O(1)

# intution : Use elements as Index and mark the visited places

def solve(arr):
    n = len(arr)
    rep = miss = 0
    for i in range(n):
        if arr[abs(arr[i]) - 1] > 0:
            arr[abs(arr[i]) - 1] = -arr[abs(arr[i]) - 1]

        else:
            rep = -arr[i]


    for i in range(n):
        if arr[i] > 0:
            miss = i + 1


    return rep, miss



arr = [1,3,4,3,5]
print(solve(arr))