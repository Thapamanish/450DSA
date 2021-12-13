# Time Complexity: O(N)
# Space Complexity: O(1)

# intution : two pointer technique


def solve(a, n):
    low = 0
    high = n - 1
    leftMax = 0
    rightMax = 0
    result = 0

    while low <= high:
        if a[low] < a[high]:
            if a[low] > leftMax:
                leftMax = a[low]

            else:
                result += leftMax - a[low]
            
            low += 1

        else:
            if a[high] > rightMax:
                rightMax = a[high]

            else:
                result += rightMax - a[high]
            
            high -= 1

    return result






arr = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
n = len(arr)
 
print("Maximum water that can be accumulated is ",
        solve(arr, n))