# Time Complexity: O(n), n = length of expression
# Space Complexity: O(n)

# intution : use the stack and its property


def areBracketsBalanced(expr):
    stack = []
 
    for char in expr:
        if char in ["(", "{", "["]:
 
            stack.append(char)

        else:
            if not stack:
                return False

            current_char = stack.pop()

            if current_char == '(' and char != ')':
                return False

            if current_char == '{' and char != '}':
                return False

            if current_char == '[' and char != ']':
                return False
 
    if stack:
        return False

    return True
 

expr = "{()}[]"
if areBracketsBalanced(expr):
    print("Balanced")
else:
    print("Not Balanced")