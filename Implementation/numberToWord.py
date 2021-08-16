# https://www.geeksforgeeks.org/convert-number-to-words/

class Solution:
    def toWords(self, n, s):
        one = ['', 'one ', 'two ', 'three ', 'four ', 'five ', 'six ', 'seven ',
            'eight ', 'nine ', 'ten ', 'eleven ', 'twelve ', 'thirteen ', 'fourteen ',
            'fifteen ', 'sixteen ', 'seventeen ', 'eighteen ', 'nineteen ']
            
        ten = ['', '', 'twenty ', 'thirty ', 'forty ', 'fifty ', 'sixty ', 'seventy ', 
                'eighty ', 'ninety ']
        words = ''
        if n > 19:
            words = ten[n // 10] + one[n % 10]
        else:
            words = one[n]
            
        if n:
            words += s
            
        return words
        
    def convertToWords(self, n):
        result = ''
        
        result += self.toWords(n// 10000000, 'crore ')
        result += self.toWords((n // 100000) % 100, 'lakh ')
        result += self.toWords((n // 1000) % 100, 'thousand ')
        result += self.toWords((n // 100) % 10, 'hundred ' )
        
        if n > 100 and n % 100:
            result += 'and '
            
        result += self.toWords(n % 100, '')
        return result




result = Solution()
print(result.convertToWords(11111))
print(result.convertToWords(12345678))