# Time complexity : O(m + n)
# Space complexity : O(m + n)

def unionAndIntersection(arr1, arr2, m, n):
    i = 0
    j = 0
    ansU = []
    ansI = []
    while i < m and j < n:
        if arr1[i] < arr2[j]:
            ansU.append(arr1[i])
            i += 1
        elif arr1[i] > arr2[j]:
            ansU.append(arr2[j])
            j += 1

        else:
            ansU.append(arr1[i])
            ansI.append(arr1[i])
            i += 1
            j += 1


    while i<m:
        ansU.append(arr1[i])
        i += 1

    while j<n:
        ansU.append(arr2[j])
        j += 1

    return ansU, ansI





arr1 = [1, 2, 4, 5, 6]
arr2 = [2, 3, 5, 7]

print(unionAndIntersection(arr1, arr2, len(arr1), len(arr2)))