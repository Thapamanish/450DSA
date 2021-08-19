def mergeSort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2

        l = arr[:mid]
        r = arr [mid:]

        mergeSort(l)
        mergeSort(r)

        i = j = k = 0

        while i < len(l) and j < len(r):
            if l[i] < r[j]:
                arr[k] = l[i]
                i += 1

            else:
                arr[k] = r[j]
                j += 1

            k += 1

        while i < len(l):
            arr[k] = l[i]
            i += 1
            k += 1

        while j < len(r):
            arr[k] = r[j]
            j += 1
            k += 1







arr = [70, 20, -9, 100, 90, 2]
l = 0
r = len(arr)
mergeSort(arr)

print(arr)