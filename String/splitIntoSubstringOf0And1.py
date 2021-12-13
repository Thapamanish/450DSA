# Time Complexity: O(N)
# Space Complexity: O(1)

# intution : traverse the string and store the count

def maxSubStr(string, n):
    count0 = 0
    count1 = 0
    cnt = 0

    for char in string:
        if char == '0':
            count0 += 1
        else:
            count1 += 1

        if count0 == count1:
            cnt += 1

    return cnt
 
 
string = "0100110101"
n = len(string)
print(maxSubStr(string, n))