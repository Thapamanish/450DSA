# Time complexity: O(n). 
                  
# Auxiliary Space: O(n). 

# intution : use LPS algorithm

def computeLPSArray(string):
 
    M = len(string)
    lps = [None] * M
 
    length = 0
    lps[0] = 0 

    i = 1
    while i < M:
     
        if string[i] == string[length]:
         
            length += 1
            lps[i] = length
            i += 1
         
        else: # (str[i] != str[len])
         
            if length != 0:
             
                length = lps[length - 1]
 
                # Also, note that we do not
                # increment i here
             
            else: # if (len == 0)
             
                lps[i] = 0
                i += 1
 
    return lps
 

def solve(string):
 
    revStr = string[::-1]
 
    # Get concatenation of string,
    # special character and reverse string
    concat = string + '$' + revStr

 
    # Get LPS array of this
    # concatenated string
    lps = computeLPSArray(concat)
 
    # By subtracting last entry of lps
    # vector from string length, we
    # will get our result
    return len(string) - lps[-1]
 


string = "AACECAAAA"
print(solve(string))
