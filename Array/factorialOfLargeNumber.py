# Time complexity: O(N^2)
# Space complexity: O(M)

#intution : it's like mupltipying two number using list


 
import sys
 
def multiply(x, res,resSize):
     
    carry = 0
    i = 0

    while i < resSize :
        prod = res[i] *x + carry
        res[i] = prod % 10
        carry = prod//10
        i = i + 1
 

    while carry:
        res[resSize] = carry % 10
        carry = carry // 10
        resSize = resSize + 1
         
    return resSize


def factorial( n) :
    res = [None]*500
    res[0] = 1
    resSize = 1
    x = 2

    while x <= n :
        resSize = multiply(x, res, resSize)
        x = x + 1
     
    print ("Factorial of given number is")
    i = resSize-1
    while i >= 0 :

        sys.stdout.write(str(res[i]))
        sys.stdout.flush()
        i = i - 1
         

factorial(5)