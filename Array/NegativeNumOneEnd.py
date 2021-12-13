# Question : program to move all negative numbers to beginning and positive to end

# Time Complexity: O(n)

# Space Complexity : O(1)

# Intution : use two pointer technique (quick sort partitioning)


# def solve(arr, n):
#     low = 0
#     high = n - 1
#     while low <= high:
#         if arr[low] < 0 and arr[high] > 0:
#             low += 1
#             high -= 1

#         elif arr[low] > 0 and arr[high] < 0:
#             arr[low], arr[high] = arr[high], arr[low]
#             high -= 1

#         elif arr[low] < 0 and arr[high] < 0:
#             low += 1

#         else:
#             high -= 1



#     return arr


def solve(arr, n):
    j = 0
    for i in range(n):
        if arr[i] < 0:
            arr[i], arr[j] = arr[j], arr[i]
            j += 1

    return arr

arr=[-12, 11, -13, -5,6, -7, 5, -3, 11]
print(solve(arr, len(arr)))
