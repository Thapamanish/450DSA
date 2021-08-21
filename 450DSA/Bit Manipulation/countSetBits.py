
 # Brian Kernighan’s Algorithm

def countSetBit(n):
    if n == 0:
        return 0
    
    return 1 + countSetBit(n & (n - 1))




num = 8
print(countSetBit(num))
      