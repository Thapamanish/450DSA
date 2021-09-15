# Question: Product of array except self 

# Time complexity: O(setBits)
                  
# Auxiliary Space: O(1)

# intution : Brian Kernighan’s Algorithm


# def countSetBit(n):
#     if n == 0:
#         return 0
    
#     return 1 + countSetBit(n & (n - 1))


# num = 8
# print(countSetBit(num))
      
def countSetBit(n):
    count = 0
    while n != 0:
        rsbm = n & -n #rsbm- rightmost set bit mask is 2's complement(i.e. 1's complement + 1)
        n -= rsbm
        count += 1
    return count


num = 7
print(countSetBit(num))
      