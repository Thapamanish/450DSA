# Time complexity: O(n)
                  
# Auxiliary Space: O(1)

# intution : use two pointers pointing to minEle and maxElement

def solve(arr):
    n = len(arr)
    if n == 1:
        minEle = arr[0]
        maxEle = arr[0]

    else:
        if arr[0] > arr[1]:
            minEle = arr[1]
            maxEle = arr[0]

        else:
            minEle = arr[0]
            maxEle = arr[1]

        for i in range(2, n):
            if arr[i] > maxEle:
                maxEle = arr[i]
            elif arr[i] < minEle:
                minEle = arr[i]

    return minEle, maxEle




arr = [2,3,1,5,8,4]
print(solve(arr))
