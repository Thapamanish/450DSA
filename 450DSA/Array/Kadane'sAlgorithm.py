Time complexity: O(N)
Space complexity: O(1)





def maxSubArraySum(a,size):
    ##Your code here
    meh = 0
    msf = float('-INF')
    
    for i in range(size):
        meh += a[i]
        if meh < a[i]:
            meh = a[i]
        if msf < meh:
            msf = meh
            
    return msf



a = [1,2,3,-2,5]
print(maxSubArraySum(a, len(a)))

