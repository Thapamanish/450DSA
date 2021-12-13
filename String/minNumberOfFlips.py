# Time complexity: O(n). 
                  
# Auxiliary Space: O(1). 

# intution : take minimum of when 0 is at begining and 1 at begining
     
def flip(expected):
    return '0' if expected == '1' else '1'

def solveUtil(inpStr, expected):
    count = 0
    for char in inpStr:
        if char != expected:
            count += 1

        expected = flip(expected)
   
    return count

def solve(inpStr):
    return min(solveUtil(inpStr, '0'), solveUtil(inpStr, '1'))


inpStr = '1001'

print(solve(inpStr))
