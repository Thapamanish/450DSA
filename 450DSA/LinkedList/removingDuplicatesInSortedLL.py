# Question: write a program to remove duplicates from sorted linked list

# Time complexity: O(n) 
                  
# Auxiliary Space: O(1)

# intution : checks current data and next node data if found same then skips the 
            # to further data

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

    def removeDuplicates(self):
        current = self.head

        while current.next:
            if current.data != current.next.data:
                current = current.next

            else:
                current.next = current.next.next



    def printList(self):
        current = self.head
        while current:
            print(current.data, end = ' ')
            current = current.next
        print()




ll = LinkedList()
ll.pushEnd(10)
ll.pushEnd(20)
ll.pushEnd(30)
ll.pushEnd(30)
ll.pushEnd(40)
ll.pushEnd(50)
ll.pushEnd(50)

ll.printList()
ll.removeDuplicates()
ll.printList()
