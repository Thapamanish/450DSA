# Time complexity: O(2^(n * m))
# Space complexity: O(n * m)

def solve(i, j, m, n, maze, ans, move, vis, di, dj):
    # check the boundary
    if i == m - 1 and j == n - 1:
        ans.append(move)
        return 

    dir = 'DLRU'
    for index in range(4):
        nexti = i + di[index] 
        nextj = j + dj[index]

        if nexti >= 0 and nextj >=0 and nexti < m and nextj < n and not vis[nexti][nextj] and maze[nexti][nextj] == 1:
            vis[i][j] = 1
            solve(nexti, nextj, m, n, maze, ans, move + dir[index], vis, di, dj)
            vis[i][j] = 0




maze = [[1, 0, 0, 0],
         [1, 1, 0, 1], 
         [1, 1, 0, 0],
         [0, 1, 1, 1]]

vis = [[0] * len(maze[0]) for i in range(len(maze))]
di = [1, 0, 0, -1]
dj = [0, -1, 1, 0]
ans = []
if maze[0][0]:
    solve(0, 0, len(maze), len(maze[0]), maze, ans, '',vis, di, dj)

print(*ans)
