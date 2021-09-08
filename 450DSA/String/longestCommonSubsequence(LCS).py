# Time Complexity: O(m * n)
# Space Complexity: O(m * n)

# intution : Dynamic Programming(Tabulation i.e. bottom up approach)
            # keep the track of subproblems

def lcs(X , Y):
    m = len(X)
    n = len(Y)
 
    dp = [[None]*(n+1) for i in range(m+1)]

    for i in range(m+1):

        for j in range(n+1):

            if i == 0 or j == 0 :
                dp[i][j] = 0

            elif X[i-1] == Y[j-1]:
                dp[i][j] = 1 + dp[i-1][j-1]
                
            else:
                dp[i][j] = max(dp[i-1][j] , dp[i][j-1])

    return dp[m][n]
 
 
X = "ABCDGH"
Y = "AEDFHR"
print("Length of LCS is ", lcs(X, Y))