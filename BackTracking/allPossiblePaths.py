# Time complexity: O(2^(n * m))
# Space complexity: O(n * m)

def solve(i, j, m, n, maze, ans, move, vis, di, dj):
    # check the boundary
    if i == m - 1 and j == n - 1:
        move += str(maze[m-1][n-1])
        ans.append(move)
        return 

    dir = 'DLRU'
    for index in range(2):
        nexti = i + di[index] 
        nextj = j + dj[index]

        if nexti >= 0 and nextj >=0 and nexti < m and nextj < n and not vis[nexti][nextj]:
            vis[i][j] = 1
            solve(nexti, nextj, m, n, maze, ans, move + str(maze[i][j]) + ' ', vis, di, dj)
            vis[i][j] = 0




maze = [[1,2,3],
        [4,5,6],
        [7,8,9]]

vis = [[0] * len(maze[0]) for i in range(len(maze))]
di = [1, 0]
dj = [0, 1]
ans = []
if maze[0][0]:
    solve(0, 0, len(maze), len(maze[0]), maze, ans, '',vis, di, dj)

for x in ans:
    print(x)