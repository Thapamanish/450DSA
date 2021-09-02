# Time Complexity: O(n*n!) Note that there are n! permutations 
# and it requires O(n) time to print a permutation


def solve(cnt, n, wordDict, ans, cStr):
    if cnt > n:
        ans.append(cStr)
        return

    for key, value in wordDict.items():
        if value > 0:
            wordDict[key] -= 1
            solve(cnt + 1, n, wordDict, ans, cStr + key)
            wordDict[key] += 1 



string = "aabb"

wordDict = {}
for char in string:
    if char in wordDict:
        wordDict[char] += 1
    else:
        wordDict[char] = 1

ans = []
solve(1, len(string), wordDict, ans, '')
print(ans)

