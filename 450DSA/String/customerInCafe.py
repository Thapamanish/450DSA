# Time complexity: O(n) 
                  
# Auxiliary Space: O(n). 

# intution : can be used mapping or stacks to keep the track of occupied




# def solve(pcCount, customer):
#     stack  = []
#     failStack = []
#     fail = 0
#     for cus in customer:
#         if cus not in stack and len(stack) < pcCount:
#             stack.append(cus)
#         elif cus in stack:
#             stack.remove(cus)
#         else:
#             if cus not in failStack:
#                 fail += 1
#                 failStack.append(cus)


#     return fail



# customer = 'ABCBCADEED'
# pcCount = 1
# print(solve(pcCount, customer))



MAX_CHAR = 26

def runCustomerSimulation(n, seq):
 
    seen = [0] * MAX_CHAR

    res = 0
    occupied = 0   
 

    for i in range(len(seq)):
 
        ind = ord(seq[i]) - ord('A')
 
        if seen[ind] == 0:
 
            seen[ind] = 1
 
            if occupied < n:
                occupied+=1
 
                seen[ind] = 2

            else:
                res+=1
 
        else:

            if seen[ind] == 2:
                occupied-=1
            seen[ind] = 0
 
    return res
 

print(runCustomerSimulation(2, "ABBAJJKZKZ"))
print(runCustomerSimulation(3, "GACCBDDBAGEE"))
print(runCustomerSimulation(3, "GACCBGDDBAEE"))
print(runCustomerSimulation(1, "ABCBCA"))
print(runCustomerSimulation(1, "ABCBCADEED"))
