# Question : program to find a maximum and a minimum element in an array

# Time Complexity: O(n)

# Space Complexity : O(1)

# Intution : use two pointer technique and divide and conquer method(tournament method)

def solve(a, low, high, minEle, maxEle):
    if low == high:
        if minEle > a[low]:
            minEle = a[low]

        elif maxEle < a[low]:
            maxEle = a[low]

        return minEle, maxEle


    if high - low == 1:
        if a[high] < a[low]:
            if minEle > a[high]:
                minEle = a[high]

            if maxEle < a[low]:
                maxEle = a[low]

        else:
            if minEle > a[low]:
                minEle = a[high]

            if maxEle < a[high]:
                maxEle = a[high]


    mid = low + (high - low)//2

    minEle, maxEle = solve(a, low, mid, minEle, maxEle)
    minEle, maxEle = solve(a, mid + 1, high, minEle, maxEle)

    return minEle, maxEle




a = [10, 20, 0, 90, 56, -90]


minEle, maxEle = float('INF'), float('-INF')

minEle, maxEle = solve(a, 0, len(a)-1, minEle, maxEle)
print(minEle, maxEle)