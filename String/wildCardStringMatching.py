# Time complexity: O(n * m). 
                  
# Auxiliary Space: O(n * m). 

# intution : dynamic programming bottom up approach 



def strrmatch(strr, pattern, n, m):
 
    if m == 0:
        return False
 

    dp = [[False for i in range(n + 1)] for j in range(m + 1)]
 
 
    for i in range(m, -1, -1):
        for j in range(n, -1, -1):
            if i == m and j == n:
                dp[i][j] = True

            elif i == m:
                dp[i][j] = False

            elif j == n:
                if pattern[i] == '*':
                    dp[i][j] = dp[i + 1][j]
                else:
                    dp[i][j] = False

            else:

                if pattern[i] == '?':
                    dp[i][j] = dp[i + 1][j + 1]
                elif pattern[i] == '*':
                    dp[i][j] = dp[i + 1][j] or dp[i][j + 1]
                elif pattern[i] == strr[j]:
                    dp[i][j] = dp[i + 1][j + 1]
                else:
                    dp[i][j] = False 

    return dp[0][0]
           
 

 
 
strr = "geeksforgeeks"
pattern = "gee?s*"

 
if (strrmatch(strr, pattern, len(strr), len(pattern))):
    print("Yes")
else:
    print("No")