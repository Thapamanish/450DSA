# Question: write a program to reverse a linked list recursively

# Time complexity: O(n) 
                  
# Auxiliary Space: O(n)

# intution : just reverse the link

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None


    def pushEnd(self, data):
        if self.head is None:
            self.head = Node(data)
            return

        current = self.head
        while current.next:
            current = current.next

        current.next = Node(data)


    def printList(self):
        current = self.head
        while current:
            print(current.data, end = ' ')
            current = current.next

        print()

    def reverseListUtil(self, current, prev):
        if current.next is None:
            self.head = current
            current.next = prev
            return

        temp = current.next
        current.next = prev

        self.reverseListUtil(temp, current)




    def reverseList(self):
        if self.head is None or self.head.next is None:
            return
        current = self.head
        prev = None
        self.reverseListUtil(current, prev)



ll = LinkedList()
ll.pushEnd(10)
ll.pushEnd(20)
ll.pushEnd(30)
ll.pushEnd(40)
ll.pushEnd(50)
ll.pushEnd(60)
ll.printList()
ll.reverseList()
ll.printList()
