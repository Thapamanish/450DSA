# Question: kth smallest element in the array of intervals.

# Time complexity: O(nlogn) + O(n) i.e. nlogn -> sorting, n -> search
                  
# Auxiliary Space: O(n)

# intution : mergeInterval problem and math problem.

def mergeArr(arr):
    n = len(arr)
    if n == 0:
        return []
    arr.sort()

    ans = [arr.pop(0)]

    for ind in range(len(arr)):
        if ans[-1][1] > arr[ind][0]:
            ans[-1][1] = max(ans[-1][1], arr[0][1])

        else:
            ans.append(arr[ind])

    return ans


def kthsmallestElement(arr, k):
    for num in arr:

        if k <= num[1] - num[0] + 1:
            return num[0] + k - 1

        else:
            k -= (num[1] - num[0] + 1)

    return -1





arr = [[2, 6], [4, 7]]
query = [5, 8]
ans = mergeArr(arr)
for k in query: 
    print(kthsmallestElement(ans, k))