# Time complexity: O(n)
# Space complexity: O(1)

def countSetBits(n):
    mem = [0] * (n + 1)
    for i in range(1, n + 1):
        mem[i] = mem[i // 2] + (i % 2)

    return sum(mem)

print(countSetBits(4))