def DCAMin(arr, index, l):
    if index >= l - 2:
        if arr[index] < arr[index + 1]:
            return arr[index]
        else:
            return arr[index + 1]


    minNum = DCAMin(arr, index + 1, l)

    if minNum < arr[index]:
        return minNum
    else:
        return arr[index]



def DCAMax(arr, index, l):
    if index >= l-2:
        if arr[index] > arr[index + 1]:
            return arr[index]
        else:
            return arr[index + 1]


    maxNum = DCAMax(arr, index + 1, l)

    if maxNum > arr[index]:
        return maxNum

    else:
        return arr[index]






arr = [70, 60, -9, 20, 1, 10, 5]

minNum = DCAMin(arr, 0, len(arr))
maxNum = DCAMax(arr, 0, len(arr))

print('Mininum number is:', minNum)
print('Maximum number is:', maxNum) 
