# Time complexity: O(total strings * length of smallest string). 
                  
# Auxiliary Space: O(1). 

# intution : make first element as prefix and compare it with
            # the other elements.
     
def commonPrefixUtil(str1, str2):
 
    result = "";
    n1 = len(str1)
    n2 = len(str2)
 
    # Compare str1 and str2
    i = 0
    j = 0
    while i <= n1 - 1 and j <= n2 - 1:
     
        if (str1[i] != str2[j]):
            break
             
        result += str1[i]
        i += 1
        j += 1
 
    return (result)
 

def commonPrefix (arr, n):
 
    prefix = arr[0]
 
    for i in range (1, n):
        prefix = commonPrefixUtil(prefix, arr[i])
 
    return prefix
 

 
arr = ["geeksforgeeks", "geeks",
                "geek", "geezer"]
n = len(arr)

ans = commonPrefix(arr, n)

if (len(ans)):
    print ("The longest common prefix is -",
            ans);
else:
    print("There is no common prefix")