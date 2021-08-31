class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
         

def ispalindrome(head):
    temp = head
    stack = []
    ispalin = True
 
    while temp:
        stack.append(temp.data)
        temp = temp.next

    while head != None:
        i = stack.pop()
        if head.data == i:
            ispalin = True
        else:
            ispalin = False
            break
 
        head = head.next
         
    return ispalin

 

one = Node(1)
two = Node(2)
three = Node(3)
four = Node(4)
five = Node(3)
six = Node(2)
seven = Node(1)


one.next = two
two.next = three
three.next = four
four.next = five
five.next = six
six.next = seven
seven.next = None
 

result = ispalindrome(one)
 
print("isPalindrome:", result)