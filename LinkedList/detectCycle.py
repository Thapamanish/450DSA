# Question: write a program to detect a loop in a linked list

# Time complexity: O(n) 
                  
# Auxiliary Space: O(1)

# intution : checks for the loop using Floyd’s Cycle-Finding Algorithm

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
 
 

    
    def detectLoop(self):
        slowP = self.head
        fastP = self.head
        while slowP and fastP and fastP.next:
            slowP = slowP.next
            fastP = fastP.next.next
            if slowP == fastP:
                return True
 
 

llist = LinkedList()
llist.pushEnd(20)
llist.pushEnd(4)
llist.pushEnd(15)
llist.pushEnd(10)
 
llist.printList()
llist.head.next.next.next.next = llist.head

if(llist.detectLoop()):
    print ("Found Loop")
else:
    print ("No Loop")