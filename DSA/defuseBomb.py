# https://leetcode.com/problems/defuse-the-bomb/


class Solution:
    def decrypt(self, code, k):
        n = len(code)
        if k == 0:
            return [0] * n
        else:
            if k > 0:
                dummy = code * (n-k + 1)
            elif k < 0:
                code = code[::-1]
                dummy = code * (n - abs(k) + 1)

            for i in range(len(code)):
                code[i] = sum(dummy[i + 1: i + abs(k) + 1])
            return code if k > 0 else code[::-1]



g = Solution()

print(g.decrypt([2, 4, 9, 3], -2)) 
print(g.decrypt([5,7,1,4], 3))
print(g.decrypt([1, 2, 3, 4], 0)) 
