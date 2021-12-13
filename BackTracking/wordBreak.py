# Time Complexity: O(2 ^ n)
# Space Complexity: O(n)

# intution: call the recursive function including the char only if 
#           it is in the dictionary

def wordBreakUtil(words, result):
    if not words:
        ans.append(result)
        return

    for i in range(1, len(words) + 1):
        prefix = words[:i]

        if prefix in wordDict:
            wordBreakUtil(words[i:], result + prefix + ' ')






def wordBreak(words):
    return wordBreakUtil(words, '')



wordDict = {"mobile", "samsung", "sam", "sung", "man",
            "mango", "icecream", "and", "go", "i", "love", "ice", "cream"}

ans = []

wordBreak('iloveicecreamandmango')
for i in ans:
    print(i)




# def wordBreak(WordDict, str1, dp):
#     n = len(str1)
 
#     if n == 0:
#         return True

#     if dp[n] == -1:
#         dp[n] = 0
 
#         for i in range(1, n + 1):
#             prefix = str1[:i]
 
#             if prefix in wordDict and wordBreak(wordDict, str1[i:], dp):
#                 dp[n] = 1
#                 return True
 
#     return dp[n] == 1
 
 


# wordDict = {"self", "th", "is", "famous", "Word",
#         "break", "b", "r", "e", "a", "k", "br",
#         "bre", "brea", "ak", "problem"}

# str1 = "Wordbreakproblem"

# dp = [-1] * (len(str1) + 1)

# if wordBreak(wordDict, str1, dp):
#     print("The string can be segmented")
# else:
#     print("The string can't be segmented")