# Question : program to reverse an array or string

# Time Complexity: O(n)

# Space Complexity : O(1)

# Intution : use two pointer technique 



def reverseArray(a, start, end):
    # if start >= end:
    #     return 

    # a[start], a[end] = a[end], a[start]

    # reverseArray(a, start + 1, end - 1)

    while start <= end:
        a[start], a[end] = a[end], a[start]
        start += 1
        end -= 1



a = [1, 2, 3, 4, 5, 6, 7]
print(a)
reverseArray(a, 0, len(a) - 1)
print(a)