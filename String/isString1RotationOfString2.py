# Time Complexity: O(N)
# Space Complexity: O(1)
# By kmp algorithm

def solve(str1, str2):
    str1 = str1 * 2
    if str2 in str1:
        # print(str1.index(str2))
        return True
    else:
        return False


str1 = 'mypencil'
str2 = 'encilmyp'
print(solve(str1, str2))