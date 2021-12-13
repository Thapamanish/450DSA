# Time complexity: O(N)
# Space complexity: O(1)

# intution : Kadane's alogrithm + keep track of minimum ending here

def maxSubArraySum(a,n):
    maxEH = 1
    minEH = 1
    msf = float('-INF')

    for i in range(n):
        if a[i] == 0:
            maxEH = 1
            minEH = 1

        temp = maxEH
        maxEH = max(a[i], a[i] * maxEH, a[i] * minEH)
        minEH = min(a[i], a[i] * temp, a[i] * minEH)

        msf = max(msf, maxEH)

    return msf


a = [1,2,3,-2,5]
print(maxSubArraySum(a, len(a)))