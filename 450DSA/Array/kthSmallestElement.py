# Question : program to find the kth smallest element

# Time Complexity: O(k * log(n)) i.e. log(n) for heapifying the array

# Space Complexity : O(1)

# Intution : use min heap


import heapq
from heapq import heappop

def solve(arr, k):
	heapq.heapify(arr)

	while k > 1:
		heappop(arr)
		k -= 1

	return arr[0]



arr = [7, 4, 6, 3, 9, 1]
k = 4
print(solve(arr, k))