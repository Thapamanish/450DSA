def reverseArray(a, start, end):
    if start >= end:
        return 

    a[start], a[end] = a[end], a[start]

    reverseArray(a, start + 1, end - 1)






a = [1,2,3,4,5, 6]
print(a)
reverseArray(a, 0, len(a) - 1)
print(a)