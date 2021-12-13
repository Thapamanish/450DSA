# Time complexity : O(N)
# Space complexity : O(1)
 
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None


    def lastToFirst(self):
        if not self.head or not self.head.next:
            return

        temp = self.head
        while temp.next.next:
            temp = temp.next

        temp.next.next = self.head
        self.head = temp.next
        temp.next = None


    def printList(self):
        temp = self.head
        while temp:
            print(temp.data, end = ' ')
            temp = temp.next

        print()


ll = LinkedList()
ll.head = Node(10)
ll.head.next = Node(20)
ll.head.next.next = Node(30)
ll.head.next.next.next = Node(40)
ll.head.next.next.next.next = Node(50)
ll.head.next.next.next.next.next = Node(60)


ll.printList()

ll.lastToFirst()

ll.printList()