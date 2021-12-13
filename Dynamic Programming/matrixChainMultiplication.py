# Time Complexity : O(n3)
# Space Complexity : O(n2)

def solve(mat, n):
    dp = [[0] * n for i in range(n)]
    
    for cl in range(2, n):
        for l in range(1, n - cl + 1):
            r = l + cl - 1
            dp[l][r] = float('INF')
            for k in range(l, r):
                temp = dp[l][k] + dp[k + 1][r] + mat[l - 1] * mat[k] * mat[r] 
                if temp < dp[l][r]:
                    dp[l][r] = temp



    return dp[1][n-1]



# mat = [1,2,3,4]
mat = [10, 30, 5, 60]

print(solve(mat, len(mat)))