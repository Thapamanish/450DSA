# Time Complexity: O(N^2)
# Space Complexity: O(N)

# intution : hashing



def find3Numbers(arr, n, target):
    ans = []
    for i in range(n):
        s = set()
        currSum = target - arr[i]
        for j in range(i + 1, n):
            if (currSum - arr[j]) in s:
                ans.append((arr[i], arr[j], currSum - arr[j]))
            s.add(arr[j])
     
    return ans if ans else False
 

arr = [1, 4, 45, 6, 10, 8]
target = 22
n = len(arr)
print(find3Numbers(arr, n, target))




# # Time Complexity: O(N^2)
# # Space Complexity: O(N)

# # intution : two pointer Technique


# def find3Numbers(A, arr_size, sum):
#     A.sort()
 
#     for i in range(0, arr_size-2):
#         l = i + 1
#         r = arr_size-1
#         while (l < r):
         
#             if( A[i] + A[l] + A[r] == sum):
#                 print("Triplet is", A[i],
#                      ', ', A[l], ', ', A[r]);
#                 return True
             
#             elif (A[i] + A[l] + A[r] < sum):
#                 l += 1
#             else: # A[i] + A[l] + A[r] > sum
#                 r -= 1
 
#     return False
 

# A = [1, 4, 45, 6, 10, 8]
# sum = 22
# arr_size = len(A)
 
# find3Numbers(A, arr_size, sum)
