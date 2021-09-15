# Time complexity: O(NlogN) + O(N) => O(NlogN) for sorting and O(N) for linear traversal 
# Space somplexity: O(1) -> generally output array isnot considerd as 
                    # auxiliary space 
def merge(intervals):
    intervals.sort()
    if len(intervals) == 0:
        return -1
    ans = []
    ans.append(intervals.pop(0))
    for ind, num in enumerate(intervals):
        if num[0] <= ans[-1][1]:
            ans[-1][1] = max(num[1], ans[-1][1])

        else:
            ans.append(list(num))

    return ans



intervals = [[1,4],[7,7] ,[0,6]]
print(merge(intervals))