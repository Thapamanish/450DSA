# Time complexity: O(N)
# Space complexity: O(N)

#intution : use hashing to store the frequencing of the numbers

def countOccurence(arr,n,k):
    numDict = {}
    for num in arr:
        if num in numDict:
            numDict[num] += 1
        else:
            numDict[num] = 1
            
    ans = []    
    for key, value in numDict.items():
        if value > (n // k):
            ans.append(key)
            
    return ans



arr = [1,2,3,4,3,2,1,2,3]
k = 4
print(countOccurence(arr, len(arr), k))