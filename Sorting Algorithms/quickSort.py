def partition(start, end, arr):
    pivot_index = start
    pivot = arr[start]

    while start < end:
        while start < len(arr) and arr[start] <= pivot:
            start += 1

        while arr[end] > pivot:
            end -= 1

        if start < end:
            arr[start], arr[end] = arr[end], arr[start]

    arr[pivot_index], arr[end] = arr[end], arr[pivot_index]


    return end


def quickSort(start, end, arr):
    if start < end:
        p = partition(start, end, arr)


        quickSort(start, p - 1, arr)
        quickSort(p + 1, end, arr)




arr = [10,4, 20 , 80, 100, 2, 6]

quickSort(0, len(arr) - 1, arr)

print(*arr)