# Time complexity: O((2 ^ N) * K)
# Space complexity: O(2 ^ N)

def solve(i, arr, K, nos, ans):
    global result
    if i == len(arr):
        if nos == K:
            flag = True
            for j in range(K -1):
                if sum(ans[j]) != sum(ans[j + 1]):
                    flag = False
                    break
            if flag:    
                for j in range(K):
                    result.append(list(ans[j]))
            
        return 




    for j in range(K):
        if len(ans[j]) > 0:
            ans[j].append(arr[i])
            solve(i + 1, arr, K, nos, ans)
            ans[j].pop()

        else:
            ans[j].append(arr[i])
            solve(i + 1, arr, K, nos + 1, ans)
            ans[j].pop()
            break


arr = [2, 1, 4, 5, 6]
K = 3
ans = []
for i in range(K):
    ans.append([])
result = []
solve(0, arr, K, 0, ans)
print(result)


