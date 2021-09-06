# Time Complexity: O(N)
# Space Complexity: O(N)

# intution : traverse from end to find maxPrice and traverse
#             from the beginning to find the minPrice

def maxProfit(price, n):
    profit = [0]*n
    maxPrice = price[n-1]
 
    for i in range(n-2, 0, -1):
        if price[i] > maxPrice:
            maxPrice = price[i]

        profit[i] = max(profit[i+1], maxPrice - price[i])

    minPrice = price[0]
 
    for i in range(1, n):
        if price[i] < minPrice:
            minPrice = price[i]
 
        profit[i] = max(profit[i-1], profit[i]+(price[i]-minPrice))

    result = profit[n-1]
 
    return result
 
 
price = [2, 30, 15, 10, 8, 25, 80]
print("Maximum profit is", maxProfit(price, len(price)))