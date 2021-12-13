# Question: Product of array except self 

# Time complexity: O(n)
                  
# Auxiliary Space: O(1)

# intution : store product at the ans list and reinsert from the end(i.e. concept of two
                #list technique, one storing product from left to right another from right
                #to left)


def solve(arr):
    n = len(arr)
    if n < 1:
        return 'invalid'

    product = 1
    ans = []

    for num in arr:
        product *= num
        ans.append(product)

    product = 1

    for i in range(n - 1, 0, -1):
        ans[i] = ans[i - 1] * product
        product *= arr[i]

    ans[0] = product
    return ans


arr = [1, 0]
print(solve(arr))

# def solve(arr):
#     n = len(arr)
#     if n <= 1:
#         return 'Invalid input'
#     countZero = 0
#     totalProd = 1
#     for num in arr:
#         if num:
#             totalProd *= num
#         else:
#             countZero += 1

#     ans = []
#     for num in arr:
#         if num and countZero == 0:
#             ans.append(totalProd // num)

#         elif not num and countZero - 1 == 0:
#             ans.append(totalProd)

#         else:
#             ans.append(0)

#     return ans

# arr = [1, 0]
# print(solve(arr))