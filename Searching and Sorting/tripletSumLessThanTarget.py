#Question: Count triplets with sum smaller than a given value

# Time complexity: O(n^2)
                  
# Auxiliary Space: O(1)

# intution : similar to three sum and four sum problem


def solve(arr, target):
    n = len(arr)
    arr.sort()
    count = 0
    for i in range(n):
        front = i + 1
        back = n - 1
        while front < back:
            twoSum = arr[front] + arr[back]
            if twoSum + arr[i] >= target:
                back -= 1
            else: # twoSum < target2:
                count += (back - front)
                front += 1



    return count





arr = [5, 1, 3, 4, 7] #1,3,4,5,7
x = 12
print(solve(arr, x))