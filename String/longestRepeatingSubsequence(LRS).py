# Time Complexity: O(n^2)
# Space Complexity: O(n^2)

# intution : LCS excluding the char at same index
def lrs(X):
    n = len(X)
    dp = [[None]*(n+1) for i in range(n+1)]

    for i in range(n+1):

        for j in range(n+1):

            if i == 0 or j == 0 :
                dp[i][j] = 0

            elif X[i-1] == X[j-1] and i != j:
                dp[i][j] = 1 + dp[i-1][j-1]

            else:
                dp[i][j] = max(dp[i-1][j] , dp[i][j-1])

    return dp[n][n]
 
 
X = "XXX"
print("Length of LCS is ", lrs(X))