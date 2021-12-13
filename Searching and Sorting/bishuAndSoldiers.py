# Question: bishu and the soldiers. 

# Time complexity: O(m * n) i.e. n -> array length, m -> no of rounds
                  
# Auxiliary Space: O(1)

# intution : linear search and add the count and element when found less than
            # the power



def solve(arr, power):
    n = len(arr)
    no_round = len(power)
    while no_round:
        bishu = power.pop(0)
        count = 0
        ans = 0

        for num in arr:
            if bishu >= num:
                ans += num
                count += 1
        no_round -= 1
        print(count, ans)



arr = [1,2,3,4,5,6,7]
power = [3, 10 , 2]
solve(arr, power)