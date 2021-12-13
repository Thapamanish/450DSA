# Question : program to minimize the height between longest and shortest tower

# Time Complexity: O(n)

# Space Complexity : O(1)

# Intution : use two variable storing value of smallest and biggest tower. 



def solve(a, k):
    n = len(arr)
    ans = a[n - 1] - a[0]
    small, big = 0, 0

    for i in range(1, n):
        small = min(a[0] + k, a[i] - k)
        big = max(a[n - 1] - k, a[i - 1] + k)
        ans = min(ans, big - small)


    return ans



arr = [1, 1, 8, 10]
print(solve(arr, 2))
