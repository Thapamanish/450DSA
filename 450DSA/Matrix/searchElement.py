def searchMatrix(matrix, target):
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == target:
                return True
    return False



print(searchMatrix([[1,3]], 3))