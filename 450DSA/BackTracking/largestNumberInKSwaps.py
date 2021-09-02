# Time complexity: O((N^2)^k)
# Space complexity: O(N)

def swap(string, i, j):
 
    return (string[:i] + string[j] +
            string[i + 1:j] +
            string[i] + string[j + 1:])
 

def findMaximumNum(string, k, maxm):

    if k == 0:
        return
 
    n = len(string)
 
    for i in range(n - 1):
 
        for j in range(i + 1, n):

            if string[i] < string[j]:
 

                string = swap(string, i, j)
 
                if string > maxm[0]:
                    maxm[0] = string
 
                findMaximumNum(string, k - 1, maxm)
 
                string = swap(string, i, j)
 

string = "129814999"
k = 4
maxm = [string]
findMaximumNum(string, k, maxm)
print(maxm[0])
 