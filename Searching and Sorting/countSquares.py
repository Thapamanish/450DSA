# Time complexity: O(sqrt(n))
                  
# Auxiliary Space: O(1) 

# intution : iterate until i * i

def solve(n):
	count = 0
	i = 1
	while i * i < n:
		count += 1
		i += 1

	return count


print(solve(9))