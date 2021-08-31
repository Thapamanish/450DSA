# Time complexity : O(nlogn)
# Space complexity : O(1)


def solve(a, k):
    n = len(arr)
    ans = a[n - 1] - a[0]
    small, big = 0, 0

    for i in range(1, n):
        small = min(a[0] + k, a[i] - k)
        big = max(a[n - 1] - k, a[i - 1] + k)
        ans = min(ans, big - small)


    return ans




arr = [1, 5, 8, 10]
print(solve(arr, 4))
