def solve(coins, amount):
    n = len(coins)
    dp = [[0] * (amount + 1) for i in range(n + 1)]

    for i in range(n + 1):
        for j in range(amount + 1):
            if j == 0:
                dp[i][j] = 0
            elif i == 0:
                dp[i][j] = 1e5
            elif coins[i - 1] > j:
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = min(1 + dp[i][j - coins[i - 1]], dp[i - 1][j])


    if dp[n][amount] > 1e4:
        return -1
    else:
        return dp[n][amount]




coins = [1,2,3]
print(solve(coins, 4))
print(solve(coins, 11))
print(solve(coins, 17))