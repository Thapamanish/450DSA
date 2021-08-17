
# https://www.geeksforgeeks.org/distinct-strings-odd-even-changes-allowed/

MAX_CHAR = 26


def encoding(string):
    hashE = [0] * MAX_CHAR
    hashO = [0] * MAX_CHAR
    for i in range(len(string)):
        c = string[i]
        if i & 1:
            hashO[ord(c) - ord('a')] += 1
        else:
            hashE[ord(c) - ord('a')] += 1



    encodingChar = ""

    for i in range(MAX_CHAR):
        encodingChar += str(hashE[i])
        encodingChar += '-'
        encodingChar += str(hashO[i])
        encodingChar += '-'

    return encodingChar



def isEqual(stringList):
    encoded1 = encoding(stringList[0])
    encoded2 = encoding(stringList[1])

    if encoded1 == encoded2:
        return True
    else:
        return False


stringList = ['abc', 'cba']
print(isEqual(stringList))

