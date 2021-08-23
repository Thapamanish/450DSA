
def wordBreakUtil(words, n,  result):
    for i in range(1, n + 1):
        prefix = words[:i]


        if prefix in wordDict:
            if i == n:
                result += prefix
                ans.append(result)
                return


            wordBreakUtil(words[i:], n - i, result + prefix + ' ')






def wordBreak(words):
    return wordBreakUtil(words, len(words), '')



wordDict = {"mobile", "samsung", "sam", "sung", "man",
            "mango", "icecream", "and", "go", "i", "love", "ice", "cream"}

ans = []

wordBreak('iloveicecreamandmango')
for i in ans:
    print(i)

