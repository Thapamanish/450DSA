def medianMatrix(matrix, r, c):
    ans = []
    for i in range(r):
        for j in range(c):
            ans.append(matrix[i][j])
            
    ans.sort()
    medianIndex = (len(ans) - 1) // 2
    return ans[medianIndex]

M = [[1, 3, 5], 
       [2, 6, 9], 
       [3, 6, 9]]
print(medianMatrix(M , len(M), len(M[0])))