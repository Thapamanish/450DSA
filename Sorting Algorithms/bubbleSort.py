def bubbleSort(arr):
    n = len(arr)
    for i in range(n - 1):
        flag = False
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                flag = True
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

        if flag == False:
            return arr



print(bubbleSort([64, 34, 25, 12, 22, 11, 90]))