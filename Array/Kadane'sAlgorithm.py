# Question : program to find the maximum subarray sum

# Time Complexity: O(n)

# Space Complexity : O(1)

# Intution : keep a track of current sum

def maxSubArraySum(a,size):
    meh = 0
    msf = float('-INF')
    
    for i in range(size):
        meh = max(meh + a[i], a[i])

        msf = max(msf, meh)
            
    return msf


a = [1,2,3,-2,5]
print(maxSubArraySum(a, len(a)))

