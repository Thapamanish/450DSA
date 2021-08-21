class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.head = None



    def push(self, data):
        if self.head is None:
            self.head = Node(data)
            return 

        temp = self.head
        self.head = Node(data)
        self.head.next = temp


    def popOut(self):
        if self.head is None:
            return "No element to pop"

        popElement = self.head
        self.head = self.head.next
        return popElement.data

    def peek(self):
        if self.head is None:
            return "Nothing to peek"

        return self.head.data

    def printStack(self):
        if self.head is None:
            print("Nothing to print")
            return 
        
        current = self.head
        while current:
            print(current.data, end = ' ')
            current = current.next
        print()



stack = Stack()
stack.printStack()
print('popped element:', stack.popOut())
print('top element:',stack.peek())
stack.push(10)
stack.push(20)
stack.push(30)
stack.push(40)
stack.push(50)
stack.printStack()
print('top element:',stack.peek())
print('popped element:', stack.popOut())
stack.printStack()
print('top element:',stack.peek())