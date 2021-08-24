def unique(arr):
    sums = 0

    for num in arr:
        sums = sums ^ num

    sums = sums & -sums

    sum1 = 0
    sum2 = 0

    for i in range(len(arr)):
        if arr[i] & sums > 0:
            sum1 = sum1 ^ arr[i]

        else:
            sum2 = sum2 ^ arr[i]


    return sum1, sum2







arr = [1,2,3,4,3,1,5,4]
n = len(arr)

print(unique(arr))