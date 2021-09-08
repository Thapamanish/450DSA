# Time Complexity: O(2^n) where n is no. of char in string
# Space Complexity: O(n)

# intution : take an element in consideration or not

def printSubsequence(inp, out, ans):
 
    if len(inp) == 0:
        ans.append(out)
        return
 
    printSubsequence(inp[1:], out+inp[0], ans)
 
    printSubsequence(inp[1:], out, ans)
 
 
out = ""
inp = "abcd"
ans = []
printSubsequence(inp, out, ans)
print(*ans)