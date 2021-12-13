# Time complexity: O(N)
# Space complexity: O(N)

#intution : use a set to keep the track of previous element,
            #if not found just add 1 to current element until
            #the incremented element are in the set


def solve(arr, n):
    s = set(arr)
    ans = 0
    for i in range(n):
        if arr[i] - 1 not in s:
            count = arr[i]
            while count in s:
                count += 1

            ans = max(ans, count - arr[i])

    return ans







arr = [1, 9, 3, 10, 4,2 ]
print(solve(arr, len(arr)))