# Time complexity: O(2 ^ N)
# Space complexity : O(N)

def tugOfWar(arr, n, pos, set1, set2, soSet1, soSet2):
    global minDiff
    global ans
    if pos == n:
        delta = abs(soSet1 - soSet2)

        if delta < minDiff and len(set1) >= n // 2 and len(set2) >= n // 2:
            minDiff = delta
            ans = [str(set1), str(set2) , str(minDiff)]
        return 

    if len(set1) < (n + 1)// 2 :
        set1.append(arr[pos])
        tugOfWar(arr, n, pos + 1, set1, set2, soSet1 + arr[pos], soSet2)
        set1.pop()

    
    if len(set1) < (n + 1)// 2:
        set2.append(arr[pos])
        tugOfWar(arr, n, pos + 1, set1, set2, soSet1, soSet2 + arr[pos])
        set2.pop()






minDiff = float('INF')
ans = ''
arr = [23, 45, -34, 12, 0, 98, -99, 4, 189, -1, 4]
tugOfWar(arr, len(arr),  0, [], [], 0, 0)
print('The first subset is :', ans[0])
print('The second subset is :', ans[1])
print('The min difference is :', minDiff)
