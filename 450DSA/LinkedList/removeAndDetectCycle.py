# Time complexity: O(N)
# Space complexity : O(1)

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
 
 
class LinkedList:
    def __init__(self):
        self.head = None
 
 
    def detectAndRemoveLoop(self):
        if self.head is None:
            return
        if self.head.next is None:
            return
 
        slowP = self.head
        fastP = self.head
        while slowP and fastP and fastP.next:
            slowP = slowP.next
            fastP = fastP.next.next
            if slowP == fastP:
                slowP = self.head
                while slowP.next != fastP.next:
                    slowP = slowP.next
                    fastP = fastP.next
                    
                fastP.next = None
 
 
    def printList(self):
        temp = self.head
        while(temp):
            print(temp.data, end = ' ')
            temp = temp.next
 
 
# Driver program
llist = LinkedList()
llist.head = Node(50)
llist.head.next = Node(20)
llist.head.next.next = Node(15)
llist.head.next.next.next = Node(4)
llist.head.next.next.next.next = Node(10)
 
# Create a loop for testing
llist.head.next.next.next.next.next = llist.head.next.next
 
llist.detectAndRemoveLoop()
 
print("Linked List after removing loop")
llist.printList()