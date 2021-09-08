# Time Complexity: O(n)
# Space Complexity: O(1) 

# intution : store the keypad value of the alphabet in the order of
            # their occurence in a list 

def printSequence(arr, inpStr):
    n = len(inpStr)
    output = ""
     
    for i in range(n):
     
        if(inpStr[i] == ' '):
            output = output + "0"

        else:
      
            position = ord(inpStr[i]) - ord('A')
            output = output + arr[position]
   
    return output
     

alphaList = ["2", "22", "222",
       "3", "33", "333",
       "4", "44", "444",
       "5", "55", "555",
       "6", "66", "666",
       "7", "77", "777", "7777",
       "8", "88", "888",
       "9", "99", "999", "9999" ]
 
inpStr = "GEEKSFORGEEKS";
print( printSequence(alphaList, inpStr))