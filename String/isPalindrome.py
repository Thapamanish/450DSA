def isPalindrome(string):
    if string == string[::-1]:
        return True
    else:
        return False


print(isPalindrome('abba'))
print(isPalindrome('abbaa'))