
def solve(arr):
    ans = []
    for i in range(len(arr)):
        if i + 1 == arr[i]:
            ans.append(arr[i])

    return ans




arr = [5,2,3,5,2,6,7,9]
print(solve(arr))