# https://practice.geeksforgeeks.org/problems/nearest-power0840/1
import math
def nearestPower(A, B):
    lowestPower = math.log(B) / math.log(A)
    M = pow(A, math.floor(lowestPower))
    N = M * A
    if B - M < N - B:
        return M
    else:
        return N

print(nearestPower(2, 4))