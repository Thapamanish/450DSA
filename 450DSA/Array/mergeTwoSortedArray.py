# Question : program to merge two sorted arrays

# Time Complexity: O(m * n)

# Space Complexity : O(1)

# Intution : use two pointer technique 

a = [1,3,5,7]
b = [2,4,6,8]
i = 0
while a and b and i < len(a):
    if a[i] > b[0]:
        a[i], b[0] = b[0], a[i]
        b.sort()
        i += 1

    else:
        i += 1
print(a, b)

