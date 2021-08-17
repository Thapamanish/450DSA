# https://www.geeksforgeeks.org/write-your-own-atoi/

def atoi(string):
    # Code here
    num = 0
    sign = 1
    if string[0] == '-':
        sign = -1
        string = string[1:]
    for i in string:
        if ord(i) > ord('9'):
            return -1
        
        num = num * 10 + (ord(i)-ord('0'))
        
    return sign * num

print(atoi('123'))
print(atoi('123a'))
print(atoi('-123'))