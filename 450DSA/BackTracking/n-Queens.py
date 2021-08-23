
def solve(col, leftRow, upperDiagonal, lowerDiagonal, mat, ans):

    if col == N:
            temp = []
            for i in range(N):
                string = ''
                string = ''.join(mat[i])
                temp.append(string)
            ans.append(temp)
            return 



    for row in range(N):
        if leftRow[row] == 0 and lowerDiagonal[row + col] == 0 and upperDiagonal[N - 1 + col - row] == 0: 

            mat[row][col] = 'Q'
       
            leftRow[row] = 1
            lowerDiagonal[row + col] = 1
            upperDiagonal[N - 1 + col - row] = 1

            solve(col + 1, leftRow, upperDiagonal, lowerDiagonal, mat, ans)
            mat[row][col] = '-'
            leftRow[row] = 0
            lowerDiagonal[row + col] = 0
            upperDiagonal[N - 1 + col - row] = 0






N = 4
mat = [['-'] * N for i in range(N)]
leftRow = [0] * N
upperDiagonal = [0] * (2*N - 1)
lowerDiagonal = [0] * (2*N - 1)
ans = []
solve(0, leftRow, upperDiagonal, lowerDiagonal, mat, ans)
print(ans)
