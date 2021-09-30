# Question : program to merge the overlapped intervals

# Time Complexity: O(n * log(n)) + O(n) => O(n * log(n)) 
                #  for sorting and O(N) for linear traversal

# Space Complexity :  O(1) -> generally output array isnot considerd as 
                    # auxiliary space 

# Intution : sort the interval and check the end time of first interval with
            # the start time of second interval


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
            ans.append(num)

    return ans


intervals = [[1,4],[7,7] ,[0,6]]
print(merge(intervals))