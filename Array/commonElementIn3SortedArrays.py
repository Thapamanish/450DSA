# Time Complexity: O(n1 + n2 + n3)
# Space Complexity: O(n1 + n2 + n3)

def solve(A, B, C):
    common = []
    i = j = k = 0

    while i < len(A) and j < len(B) and k < len(C):
        if A[i] == B[j] == C[k]:
            if A[i] not in common:
                common.append(A[i])
            i += 1
            j += 1
            k += 1

        elif A[i] < B[j]:
            i += 1
        elif B[j] < C[k]:
            j += 1
        else: 
            k += 1

    return common if common else [-1]  


A = [1, 5, 10, 20, 20, 40, 80,]
B = [6, 7, 20, 20,80, 100]
C = [3, 4, 15, 20, 20, 30, 70, 80, 120]
print(solve(A,B,C))