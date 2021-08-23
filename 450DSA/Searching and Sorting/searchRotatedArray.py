def search(arr, target):
    for i in range(len(arr)):
        if target == arr[i]:
            return i

    return -1


arr = [4,5,6,7,0,1,2,3]
print(search(arr, 0))