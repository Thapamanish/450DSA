# Time complexity: O(n * l)
# Space complexity: O(1)


def countAndSay(n):
    if n == 1:
        return '1'

    if n == 2:
        return '11'


    s = '11'

    for i in range(3, n + 1):
        s += '$'
        l = len(s)
        cnt = 1
        temp = ''
        for j in range(1, l):
            if s[j - 1] == s[j]:
                cnt += 1
            else:
                temp += str(cnt) + s[j - 1]
                cnt = 1

        s = temp

    return s





n = 5
print(countAndSay(n))