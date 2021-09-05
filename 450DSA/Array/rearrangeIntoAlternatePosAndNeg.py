# Time Complexity: O(N*logN)
# Space Complexity: O(1)
 
def rearrange(arr, n):
    arr.sort()

    i, j = 1, 1
    while j < n:
        if arr[j] > 0:
            break
        j += 1
 

    while (arr[i] < 0) and (j < n):
        arr[i], arr[j] = arr[j], arr[i]  
        i += 2     
        j += 1
     
    return(arr)
   
 
 

arr = [-5, -2, 5, 2, 4, 7, 1, 8, 0, -8]
 
print(*rearrange(arr, len(arr)))
