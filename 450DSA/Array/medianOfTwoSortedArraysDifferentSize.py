# Time Complexity: O(min(logN, logM))
# Space Complexity: O(1)

# intution : use binary search properties

def median(A, B):
       
        n = len(A)
        m = len(B)
        if (n > m):
            return Median(B, A)  # Swapping to make A smaller
 
        start = 0
        end = n
        realmidinmergedarray = (n + m + 1) // 2
 
        while (start <= end):
            mid = (start + end) // 2
            leftAsize = mid
            leftBsize = realmidinmergedarray - mid
            
            # checking overflow of indices
            leftA = A[leftAsize - 1] if (leftAsize > 0) else float('-inf')
            leftB = B[leftBsize - 1] if (leftBsize > 0) else float('-inf')
            rightA = A[leftAsize] if (leftAsize < n) else float('inf')
            rightB = B[leftBsize] if (leftBsize < m) else float('inf')
 
            # if correct partition is done
            if leftA <= rightB and leftB <= rightA:
                if ((m + n) % 2 == 0):
                    return (max(leftA, leftB) + min(rightA, rightB)) / 2.0
                return max(leftA, leftB)
 
            elif (leftA > rightB):
                end = mid - 1
            else:
                start = mid + 1
 

# arr1 = [-5, 3, 6, 12, 15]
# arr2 = [-12, -10, -6, -3, 4, 10]
arr1 = [4, 6]
arr2 = [1,2,3,5]
print("Median of the two arrays is", median(arr1, arr2))