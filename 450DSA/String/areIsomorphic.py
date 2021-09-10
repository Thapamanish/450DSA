# Time complexity: O(n). 
                  
# Auxiliary Space: O(n + n). 

# intution : use dictionary to count the corresponding character count and return False
            # if count differs at any point of time.

def areIsomorphic(str1,str2):
    m = len(str1)
    n = len(str2)
    
    if m != n:
        return False
    
    dict1 = {}
    dict2 = {}
    for i in range(n):
        dict1[str1[i]] = dict1.get(str1[i], 0) + 1        
        
        dict2[str2[i]] = dict2.get(str2[i], 0) + 1
    
        if dict1[str1[i]] != dict2[str2[i]]:
            return False
        
    return True


X = 'aab'
Y = 'xxc'

print(areIsomorphic(X, Y))
