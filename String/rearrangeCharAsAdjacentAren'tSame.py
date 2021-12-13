# Time complexity: O(n). 
                  
# Auxiliary Space: O(n + 26). 

# intution : find the element with maximum frequency and put it into the even pos
            # and put all other elements in other position.


def solve(inpStr):
    n = len(inpStr)
    if not n:
        return False
    alpha = [0] * 26
    for char in inpStr:
        alpha[ord(char) - ord('a')] += 1

    maxValue = 0
    for i in range(26):
        if alpha[i] > maxValue:
            maxValue = alpha[i]
            maxChar = chr(i + ord('a'))

    if maxValue > (n + 1) // 2:
        return False

    res = [None] * n

    ind = 0
    
    while maxValue:
        res[ind] = maxChar
        ind += 2
        maxValue -= 1

    alpha[ord(maxChar) - ord('a')] = 0


    for i in range(26):
        while alpha[i] > 0:
            if ind >= n:
                ind = 1
            res[ind] = chr(i + ord('a') )
            ind += 2
            alpha[i] -= 1


    return ''.join(res)




inpStr = 'kkbb'
print(solve(inpStr))