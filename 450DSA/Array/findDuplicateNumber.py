# Time complexity: O(N)
# Space complexity: O(1)


def solve(arr):
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
# [1,2,3,4,5,2]
print(solve(arr))
