# Time complexity: O(n * m). 
                  
# Auxiliary Space: O(n * m). 

# intution : use lcs to find longest common sequence and then substract it with respective
            # string length because it will the optimal solution than any other




def solve(x, y):
    m = len(x)
    n = len(y)

    dp = [[0 for i in range(m + 1)] for j in range(n + 1)]

    for i in range(n + 1):
        for j in range(m + 1):
            if i == 0 or j == 0:
                dp[i][j] = 0

            elif x[i - 1] == y[j - 1]:
                dp[i][j] = 1 + dp[i - 1][j - 1]

            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])


    
    c1 = len(x) - dp[m][n]
    c2 = len(y) - dp[m][n]
    return c1 + c2



X = "ABCDGH"
Y = "AEDFHR"
print("Total cost operation ", solve(X, Y))
 