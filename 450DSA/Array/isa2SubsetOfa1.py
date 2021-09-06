# Time Complexity: O(N * M)
# Space Complexity: O(1)

# intution : use membership operator(i.e. in)

def solve(a1, a2):
    for num in a2:
        if num not in a1:
            return False

    return True


a1 = [11, 1, 13, 21, 3, 7]
a2 = [11, 3, 7, 1]
print(solve(a1, a2))


# # Time Complexity: O(M + N)
# # Space Complexity: O(M + N)

# # intution : use a set to track the length of a1 and a2

# def solve(a1, a2):
#     s = set(num for num in a1)
#     a1Len = len(s)
    
#     for num in a2:
#         s.add(num)
    
#     if a1Len == len(s):
#         return True 
#     return False


# a1 = [11, 1, 13, 21, 3, 7]
# a2 = [11, 3, 7, 1]
# print(solve(a1, a2))