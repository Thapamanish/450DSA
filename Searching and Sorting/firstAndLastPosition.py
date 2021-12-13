def firstIndex(arr, low, high, x, n):
    if high >= low:
        mid = low + (high - low) // 2
        if (mid == 0 or x > arr[mid -1]) and arr[mid] == x:
            return mid
        elif x <= arr[mid]:
            return firstIndex(arr, low, mid - 1, x, n)
        else:
            return firstIndex(arr, mid + 1, high, x, n)

    return -1


def lastIndex(arr, low, high, x, n):
    if high >= low:
        mid = low + (high - low) // 2
        if (mid == n -1 or x < arr[mid + 1]) and arr[mid] == x:
            return mid
        elif x < arr[mid]:
            return lastIndex(arr, low, mid - 1, x, n)
        else:
            return lastIndex(arr, mid + 1, high, x, n )

    return -1



arr = [1,3,4,4,5,5,5,5,5,7,8,9]
x = 5

print(firstIndex(arr, 0, len(arr) - 1, x, len(arr)), end = ' ')
print(lastIndex(arr, 0, len(arr) - 1, x, len(arr)), end = ' ')

