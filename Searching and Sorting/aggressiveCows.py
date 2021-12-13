# Question: Find the largest minimal distance between the stalls of the cows
            #(Aggressive Cows)

# Time complexity: O(n * log(hig - low)
                  
# Auxiliary Space: O(1)

# intution : use binary search property for finding the gap


def solve(arr, cows):
    n = len(arr)
    arr.sort()
    low = 1
    high = arr[n - 1]
    best = 0
    while low <= high:
        mid = (low + high + 1) // 2
        cnt = 1
        left = 0
        for i in range(1, n):
            if cnt == cows:
                break
            if arr[i] - arr[left] >= mid:
                cnt += 1
                left = i



        if cnt == cows:
            best = mid
            low = mid + 1

        else:
            high = mid - 1


    return best 





arr = [1, 2, 8, 4, 9]
cows = 3
print(solve(arr, cows))