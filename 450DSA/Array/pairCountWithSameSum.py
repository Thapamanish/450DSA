# Time Complexity: O(N)
# Space Complexity: O(N)

def getPairsCount(arr, k):
    numDict = {}
    count = 0
    for i in range(len(arr)):
        if k - arr[i] in numDict:
            count += numDict[k - arr[i]]
        
        if arr[i] in numDict:
            numDict[arr[i]] += 1
        else:
            numDict[arr[i]] = 1
            
    return count



arr = [9, 7, 53, 41, 4, 97, 75, 30, 54, 61, 9, 8, 14, 50, 95, 38, 12, 38, 44, 2, 78, 71, 97, 67, 10, 4, 68, 43, 47, 56, 35, 7, 62, 39, 47, 17, 36, 21, 46, 41, 34, 7]
print(getPairsCount(arr, 43))