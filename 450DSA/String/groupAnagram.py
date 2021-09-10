# Time complexity: O(n * m) where n is total strings and m in length of strings. 
                  
# Auxiliary Space: O(n * 26). 

# intution : Use mapping for sorting the words and put them into the dictionary


def mapping(word, mainDict):
    alpha = [0] * 26
    for char in word:
        alpha[ord(char) - ord('a')] += 1


    string = ''
    for i in range(26):
        if alpha[i] > 0:
            string += chr(i + ord('a'))


    if string not in mainDict:
        mainDict[string] = [word]
    else:
        mainDict[string].append(word)




def solve(words):
    mainDict = {}
    for word in words:
        mapping(word, mainDict)

    ans = []
    for key in mainDict:
        ans.append(mainDict[key])

    return ans



words = ['act','god','cat','dog','tac']
print(solve(words))
