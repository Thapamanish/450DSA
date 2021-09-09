# Time Complexity: O(n * n)
# Space Complexity: O(n * n) 

# intution : dynamic programming keeping the track of prefix,
            # middle part and suffix. 



def solve(inpStr):
    n = len(inpStr)
    dp = [[0] * n for i in range(n)]
    
    for i in range(n):
        j = 0
        for k in range(i, n):
            if i == 0:
                dp[j][k] = 1

            else:
                if inpStr[j] == inpStr[k]:
                    dp[j][k] = 1 + dp[j][k - 1] + dp[j + 1][k]

                else:
                    dp[j][k] = dp[j][k - 1] + dp[j + 1][k] - dp[j + 1][k - 1]

            j += 1

    return dp[0][n - 1]



inpStr = 'abca'
print(solve(inpStr))
 