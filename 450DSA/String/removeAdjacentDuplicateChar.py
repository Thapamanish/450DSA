# Time complexity: O(n). 
                  
# Auxiliary Space: O(1). 

# intution : use two pointer technique 


def removeDuplicates(S):
    S = list(S)
         
    n = len(S)

    if (n < 2) :
        return
         
    j = 0
     
    for i in range(n):

        if (S[j] != S[i]):
            j += 1
            S[j] = S[i]

    j += 1
    S = S[:j]
    return S
     

         
S1 = "geeksforgeeks"
S1 = removeDuplicates(S1)
print(*S1, sep = "")
     
S2 = "aabcca"
S2 = removeDuplicates(S2)
print(*S2, sep = "")