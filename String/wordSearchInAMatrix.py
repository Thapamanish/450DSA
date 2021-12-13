# Time complexity: O(R*C*8*len(str)). 
                    # All the cells will be visited and traversed in all 8 directions, where R and C is side of matrix so time complexity is O(R*C).
# Auxiliary Space: O(1). 

# intution : traverse to each and every direction if the first element is found



     

def search2D(grid, row, col, word, R, C):
    dir = [[-1, 0], [1, 0], [1, 1], [1, -1], 
            [-1, -1], [-1, 1], [0, 1], [0, -1]]
                 
     
    # If first character of word doesn't match
    # with the given starting point in grid.
    if grid[row][col] != word[0]:
        return False
         
    # Search word in all 8 directions
    # starting from (row, col)
    for x, y in dir:
         
        # Initialize starting point
        # for current direction
        rd, cd = row + x, col + y
        flag = True
         
        # First character is already checked,
        # match remaining characters
        for k in range(1, len(word)):
             
            # If out of bound or not matched, break
            if (0 <= rd < R and
                0 <= cd < C and
                word[k] == grid[rd][cd]):
                 
                # Moving in particular direction
                rd += x
                cd += y
            else:
                flag = False
                break
         
        # If all character matched, then
        # value of flag must be false       
        if flag:
            return True
    return False
         
    # Searches given word in a given matrix
    # in all 8 directions   

def patternSearch(grid, word):
     
    # Rows and columns in given grid
    R = len(grid)
    C = len(grid[0])
    ans = []
    # Consider every point as starting point
    # and search given word
    for row in range(R):
        for col in range(C):
            if search2D(grid, row, col, word, R, C):
                ans.append([row, col])
    return ans
                     

grid = ["GEEKSFORGEEKS",
        "GEEKSQUIZGEEK",
        "IDEQAPRACTICE"]
print(patternSearch(grid, 'GEEKS'))
print(patternSearch(grid, 'EEE'))