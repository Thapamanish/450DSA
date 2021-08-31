# Time complexity : O(N)
# Space complexity : O(1)

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

        curr = self.head
        while curr.next:
            curr = curr.next

        curr.next = Node(data)


    def printList(self, head):
        curr = head
        while curr:
            print(curr.data, end = ' ')
            curr = curr.next

        print()


    def middleNode(self):
        slowP = self.head
        fastP = self.head

        while fastP and fastP.next:
            slowP = slowP.next
            fastP = fastP.next.next

        return slowP


ll = LinkedList()
ll.pushEnd(10)
ll.pushEnd(20)
ll.pushEnd(30)
ll.pushEnd(40)
ll.pushEnd(50)
ll.pushEnd(60)
ll.printList(ll.head)
middle = ll.middleNode()
ll.printList(middle)