# Time complexity: O(n^3)
                  
# Auxiliary Space: O(1)

# intution : use two loops and two pointer technique. 

def solve(arr, target):
    n = len(arr)
    if n == 0:
        return -1

    arr.sort()
    result = []
    i = 0

    for i in range(n):
        for j in range(i + 1, n):

            target2 = target - (arr[i] + arr[j])
            front = j + 1
            back = n - 1

            while front < back:
                twoSum = arr[front] + arr[back]

                if twoSum < target2:
                    front += 1

                elif twoSum > target2:
                    back -= 1

                else:
                    ans = [arr[i], arr[j], arr[front], arr[back]]
                    if ans not in result:
                        result.append(ans)
                    while front < back and arr[front] == ans[2]:
                        front += 1

                    while front < back and arr[back] == ans[3]:
                        back -= 1


    if result:
        return result

    return -1


