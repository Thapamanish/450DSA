def reverseString(string):
	start = 0
	end = len(string) - 1
	while start < end:
		string[start], string[end] = string[end], string[start]
		start += 1
		end -= 1
	print(string)



string = 'hello World'
print(list(string))
reverseString(list(string))