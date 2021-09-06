# Time Complexity: O(N)
# Space Complexity: O(1)

# intution : soring and finding minimum difference while traversing

def findMinDiff(arr, n, m):
    if (m==0 or n==0):
        return 0
 

    arr.sort()

    if (n < m):
        return -1

    minDiff = arr[n-1] - arr[0]

    for i in range(n - m + 1):
        minDiff = min(minDiff ,  arr[i + m - 1] - arr[i])
     
         
    return minDiff
 

arr = [12, 4, 7, 9, 2, 23, 25, 41,
      30, 40, 28, 42, 30, 44, 48,
      43, 50]
m = 7 # Number of students
n = len(arr)
print("Minimum difference is", findMinDiff(arr, n, m))