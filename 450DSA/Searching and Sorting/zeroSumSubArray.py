#Question: Count the sub arrays with sum 0

# Time complexity: O(n)
                  
# Auxiliary Space: O(n)

# intution : prefix Sum i.e. idea like kadane's algorithm



def solve(arr):
    n = len(arr)
    tSum = 0
    count = 0
    hashmap = {0: 1}
    for i in range(n):
        tSum += arr[i]
        if tSum in hashmap:
            count += hashmap[tSum]
            hashmap[tSum] += 1


        else:
            hashmap[tSum] = 1 

    return count 



arr = [0,0,5,5,0,0]
print(solve(arr))