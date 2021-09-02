# Time Complexity : O(8N^2).
# Space Complexity : O(N^2).



# Check if `(x, y)` is valid chessboard coordinates.
# Note that a knight cannot go out of the chessboard
def isValid(x, y):
    return not (x < 0 or y < 0 or x >= N or y >= N)
 
 
# Recursive function to perform the knight's tour using backtracking
def knightTour(visited, x, y, pos):
 
    # mark the current square as visited
    visited[x][y] = pos
 
    # if all squares are visited, print the solution
    if pos >= N * N:
        for r in visited:
            print(r)
        print()
        # backtrack before returning
        visited[x][y] = -1
        return
 
    # check for all eight possible movements for a knight
    # and recur for each valid movement
    for k in range(8):
 
        # get the new position of the knight from the current
        # position on the chessboard
        newX = x + row[k]
        newY = y + col[k]
 
        # if the new position is valid and not visited yet
        if isValid(newX, newY) and visited[newX][newY] == -1:
            knightTour(visited, newX, newY, pos + 1)
 
    # backtrack from the current square and remove it from the current path
    visited[x][y] = -1
 
 

row = [2, 1, -1, -2, -2, -1, 1, 2]
col = [1, 2, 2, 1, -1, -2, -2, -1]
# `N × N` chessboard
N = 8

# visited serves two purposes:
# 1. It keeps track of squares involved in the knight's tour.
# 2. It stores the order in which the squares are visited.
visited = [[-1 for x in range(N)] for y in range(N)]
visited[0][0] = 0
pos = 1

# start knight tour from corner square `(0, 0)`
knightTour(visited, 0, 0, pos)