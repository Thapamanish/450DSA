# Question: write a program to remove a loop in a linked list.

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
        current= self.head

        while current:
            print(current.data, end= ' ')
            current = current.next

        print()


    def removeCycle(self):
        if self.head is None:
            return -1

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


 

ll = LinkedList()
ll.pushEnd(10)
ll.pushEnd(20)
ll.pushEnd(30)
ll.pushEnd(40)
ll.pushEnd(50)

ll.printList()

ll.head.next.next.next.next.next = ll.head.next.next
 
ll.removeCycle()
 
print("Linked List after removing loop")
ll.printList()