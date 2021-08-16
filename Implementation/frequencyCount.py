# https://www.geeksforgeeks.org/print-characters-frequencies-order-occurrence/

string = list('geeksforgeeks')
letterDict = {}
for letter in string:
    if letter not in letterDict:
        letterDict[letter] = 1
    else:
        letterDict[letter] += 1

for key, value in letterDict.items():
    print(key, value, sep = '', end = ' ')

