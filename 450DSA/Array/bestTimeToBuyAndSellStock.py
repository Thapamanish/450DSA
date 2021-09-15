#Question: Stock Buy Sell to Maximize Profit

# Time Complexity: O(N)
# Space Complexity: O(1)

#Intitution : Modified Kadane's Algorithm, find minEle and maxProfit

def solve(arr):
    maxProfit = 0
    minEle = float('INF')
    for i in range(len(arr)):
        minEle = min(minEle, arr[i])
        maxProfit = max(maxProfit, arr[i] - minEle)

    return maxProfit





arr = [7,1,5,3,6,4]
print(solve(arr))
