# Question : program to find a Duplicate Number in the array

# Time Complexity: O(n)

# Space Complexity : O(1)

# Intution : flyod's cycle detection algorithm


def solve(arr):
    if len(arr) == len(set(arr)):
        return -1

    slow = arr[0]
    fast = arr[0]
    while True:
        slow = arr[slow]
        fast = arr[arr[fast]]
        if slow == fast:
            break


    fast = arr[0]

    while fast != slow:
        fast = arr[fast]
        slow = arr[slow]


    return slow


arr = [1,3,4,2,2]
# arr = [1,2,3,4,5,1]
print(solve(arr))
