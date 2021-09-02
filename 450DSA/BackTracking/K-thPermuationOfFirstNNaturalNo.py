def solve(cnt, n, wordDict, ans, cStr):
    if cnt > n:
        ans.append(cStr)
        return

    for key, value in wordDict.items():
        if value > 0:
            wordDict[key] -= 1
            solve(cnt + 1, n, wordDict, ans, cStr + key)
            wordDict[key] += 1 



N = 3
string = ''
for i in range(1,N + 1):
    string += str(i)
K = 4
wordDict = {}
for char in string:
    if char in wordDict:
        wordDict[char] += 1
    else:
        wordDict[char] = 1

ans = []
solve(1, len(string), wordDict, ans, '')
if K <= len(ans):
    print(ans[K - 1])
else:
    print('invalid')
