# Time Complexity: O(N)
# Space Complexity: O(1)

# intution : Sliding window technique

def minSwap(arr, n, k) :
    count = 0
    for i in range(0, n) :
        if (arr[i] <= k) :
            count = count + 1

    print(count)
     
    bad = 0
    for i in range(0, count) :
        if (arr[i] > k) :
            bad = bad + 1

    ans = bad

    for i in range(0, n - count) :
        if (arr[i] > k) :
            bad = bad - 1
         
        if (arr[i + count] > k) :
            bad = bad + 1
         
        ans = min(ans, bad)

 
    return ans
 

arr = [2, 1, 5, 6, 3]
n = len(arr)
k = 3
print (minSwap(arr, n, k))
 
arr1 = [2, 7, 9, 5, 8, 7, 4]
n = len(arr1)
k = 5
print (minSwap(arr1, n, k))