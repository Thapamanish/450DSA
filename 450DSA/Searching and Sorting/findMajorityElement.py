# Time complexity: O(n)
                  
# Auxiliary Space: O(1)

# intution : Moore's Voting algorithm

def isMajority(majEle, arr):
    count = 0
    for num in arr:
        if num == majEle:
            count += 1

    if count > len(arr) // 2:
        return True

    return False



def solve(arr):
    n = len(arr)
    majIndex = count = 1
    for i in range(1, n):
        if arr[majIndex] == arr[i]:
            count += 1

        else:
            count -= 1

        if count == 0:
            majIndex = i
            count = 1

    if isMajority(arr[majIndex], arr):
        return arr[majIndex]
    else:
        return 'No majority element'


arr = [1,3,2,5,3,1,2,2,2,2,2]
print(solve(arr))