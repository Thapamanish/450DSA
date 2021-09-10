# Time complexity: O(2^n) i.e. Exponential. 
                  
# Auxiliary Space: O(n) i.e. Call Stack. 

# intution : recursively call itself.



def solve(arr, result = '', n = 0):
    if n == len(arr):
        print(result.strip())
        return

    for word in arr[n]:
        solve(arr, result + word + ' ', n + 1)



arr = [ ["you", "we",""],
        ["have", "are",""],
        ["sleep", "eat", "drink"]]

solve(arr)
 