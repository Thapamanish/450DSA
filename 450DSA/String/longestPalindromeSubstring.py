# Time complexity : O(n2)
# space complexity : O(n2)

def longestPalin(s):
    n = len(s)
    dp = [[0] * n for i in range(n)]


    for i in range(n):
        dp[i][i] = 1
    
    maxlength = 1
    start = 0
    for i in range(n - 1):
        if s[i] == s[i + 1]:
            dp[i][i+ 1] = 1
            start = i
            maxlength = 2

    for k in range(3, n + 1):
        for i in range(n - k + 1):
            j = i + k - 1

            if s[i] == s[j] and dp[i + 1][j - 1] == 1:
                dp[i][j] = 1 

                if k > maxlength:
                    maxlength =k
                    start = i

    return maxlength, s[start:start + maxlength]



s = 'forgeeksskeegfor'

print(longestPalin(s))