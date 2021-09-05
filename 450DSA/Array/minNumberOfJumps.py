# Time complexity : O(N ^ 2)
# Space complexity : O(N)

def minJumps(arr, n):
    dp = [0  for i in range(n)]


    for i in range(n - 2, -1, -1):
        if arr[i] == 0:
            dp[i] = None
            continue

        minVal = float('INF')
        steps = arr[i]
        for j in range(1, steps + 1):
            if i + j < n:
                if dp[i + j] != None and dp [i + j] < minVal:
                    minVal = dp[i + j]

    
        if minVal != float('INF'):
            dp[i] = minVal + 1
        else:
            dp[i] = None

    return dp[0]




arr = [2,1,1,1,1,2,3]
n = len(arr)
print('Minimum number of jumps to reach',
      'end is', minJumps(arr, n))