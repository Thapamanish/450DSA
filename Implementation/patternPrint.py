'''Input: n = 3
Output: 
1*2*3*10*11*12
--4*5*8*9
----6*7'''


def pattern(n):
    initial = n
    target = n * (n + 1)
    numbers = []
    for i in range(1, target + 1):
        numbers.append(i)

    i = 0
    j = len(numbers)
    target -= n

    x = 0
    ans = []
    for num in range(n - 1, -1, -1):
        result = ''
        result += '-' * x
        for m in numbers[i:initial]:
            result += str(m) + '*'
        for m in numbers[target:j]:
            result += str(m) + '*'
        ans.append(result[:-1])

        i = initial
        j = target
        target -= num
        initial += num
        x += 2
    return ans

n =5
ans = pattern(n)
for i in range(n):
    print(ans[i])