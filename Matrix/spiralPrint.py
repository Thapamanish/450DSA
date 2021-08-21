def spiralPrint(arr, m, n, i, j):
    if i >= m or j >=n:
        return 

    for p in range(j, n):
        print(arr[i][p], end = ' ')

    for p in range(i + 1, m):
        print(arr[p][n-1], end = ' ')

    if i != m - 1:
        for p in range(n - 2, j - 1, -1):
            print(arr[m - 1][p], end = ' ')

    if j != n - 1:
        for p in range(m - 2, i, -1):
            print(arr[p][j], end= ' ')

    spiralPrint(arr, m - 1, n - 1, i + 1, j + 1)






# arr = [[1, 2, 3, 4],
#        [5, 6, 7, 8],
#        [9, 10, 11, 12],
#        [13, 14, 15, 16]]
arr = [[5, 11, 30],
        [5, 19, 19]]

for x in arr:
    print(x)

print()
spiralPrint(arr, len(arr), len(arr[0]), 0, 0)