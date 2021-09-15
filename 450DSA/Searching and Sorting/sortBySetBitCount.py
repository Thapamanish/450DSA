# Question: sort the array on the basis of set bit count. 

# Time complexity: O(nlogn)
                  
# Auxiliary Space: O(n)

# intution : count the bits using kernighan's alogrithm and sort using lambda
            #function.



def solve(arr):
    n = len(arr)
    ans = []
    for i in range(n):
        count = 0 
        k = arr[i]
        while k:
            rsbm = k & -k
            k -= rsbm
            count += 1

        ans.append((count, arr[i]))
    # ans.sort(reverse = True)
    ans.sort(key = lambda x : x[0], reverse = True)
    res = []
    for i in ans:
        res.append(i[1])

    return res

arr = [9, 8, 6, 1, 11, 7, 3, 3, 10]
print(solve(arr))