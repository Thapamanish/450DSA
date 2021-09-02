# Time complexity: O(2^N * K)
# Space complexity: O(N * K)



def combinationSum(ind, target, arr, ans, temp):
    if target == 0:
        ans.append(list(temp))
        return

    if ind == len(arr):
        return 

    if arr[ind] <= target:
        temp.append(arr[ind])
        combinationSum(ind, target - arr[ind], arr, ans, temp)
        temp.pop()

    combinationSum(ind + 1, target, arr, ans, temp)





arr = [2,4,6,8]
target = 8
ans = []
temp = []
combinationSum(0, target, arr, ans, temp)
print(ans)