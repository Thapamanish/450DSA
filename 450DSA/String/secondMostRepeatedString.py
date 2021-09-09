# Time complexity: O(n * maximum string length). 
                  
# Auxiliary Space: O(n). 

# intution : take minimum of when 0 is at begining and 1 at begining
     
def secFrequent(arr):
    freq = {}
    for string in arr:
        if string in freq:
            freq[string] += 1
        else:
            freq[string] = 1
            
    firstMax = float('-INF')
    secondMax = float('-INF')

    for key, value in freq.items():
        if value > firstMax:
            secondMax = firstMax
            firstMax = value

        elif secondMax < value < firstMax:
            secondMax = value


    for key, value in freq.items():
        if value == secondMax:
            return key



seq = [ "ccc", "aaa", "ccc",
        "ddd", "aaa", "aaa" ]
print(secFrequent(seq))