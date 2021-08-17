class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None


    def pushEnd(self, data):
        newNode = Node(data)
        if self.head is None:
            self.head = newNode
            return 

        current = self.head
        while current.next:
            current = current.next

        current.next = newNode


    def printList(self):
        current = self.head
        while current:
            print(current.data, end = ' ')
            current = current.next


    def countLists(self, nodes):
        if nodes is None:
            return 0

        return 1 + self.countLists(nodes.next)

    def iscounting(self):
        return self.countLists(self.head)



ll = LinkedList()
ll.pushEnd(10)
ll.pushEnd(20)
ll.pushEnd(30)
ll.pushEnd(40)
ll.pushEnd(50)
ll.pushEnd(50)
ll.pushEnd(50)
ll.pushEnd(50)
ll.printList()
print()
print(ll.iscounting())