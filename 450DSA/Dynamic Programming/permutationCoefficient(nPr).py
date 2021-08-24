# Time Complexity: O(n*r) 
# Auxiliary Space: O(n*r)


def nPr(n, r):
    dp = [[0] * (r + 1) for i in range(n + 1)]

    for i in range(n + 1):
        for j in range(min(i, r) + 1):
            if j == 0:
                dp[i][j] = 1

            else:
                dp[i][j] = j * dp[i - 1][j - 1] + dp[i - 1][j]


    return dp[n][r]



n = 10
r = 2
print(nPr(n, r))
