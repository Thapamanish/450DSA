# Time Complexity: O(N)
# Space Complexity: O(1)

# intution : traverse the element and 
			# compare with inverse element


def palinArray(arr ,n):
    for num in arr: 
        num = str(num)
        if num != num[::-1]:
            return False
            
    return True



arr = [11,222,3333,4]
print(palinArray(arr, len(arr)))