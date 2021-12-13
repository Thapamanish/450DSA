def smallestLargest(arr, k):
    arr.sort()
    return arr[k - 1], arr[-k]


arr = [4,5,1,2,6,3]
print(*smallestLargest(arr, 4))