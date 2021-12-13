import math

# Time Complexity: O(n*k) 
# Auxiliary Space: O(n*k)


def nCr(n, k):
    dp = [[0] * (k + 1) for i in range(n + 1)]

    for i in range(n + 1):
        for j in range(min(k, i)+1):
            if j == 0 or j == i:
                dp[i][j] = 1

            else:
                dp[i][j] = math.floor((dp[i - 1][j - 1] + dp[i - 1][j]) % (1e9 + 7))



    return dp[n][k]

