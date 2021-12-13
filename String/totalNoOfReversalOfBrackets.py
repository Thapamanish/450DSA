# Time Complexity: O(n)
# Space Complexity: O(1) 

# intution : keep a track of no. of open brackets. 


def findMinInversions(exp):
 
    if len(exp) % 2:
        return -1
 
    inversions = 0          # stores total inversions needed
    open = 0                # stores the total number of opening braces
 
    for i in range(len(exp)):
 
        if exp[i] == '{':
            open = open + 1
 
        else:

            if open:
                open = open - 1 

            else:
               
                inversions = inversions + 1    
                open = 1                       

    return inversions + open // 2
 

 
exp = '{{}{{}{{'
inv = findMinInversions(exp)

if inv != -1:
    print('The minimum number of inversions needed is', inv)
else:
    print('Invalid input')
