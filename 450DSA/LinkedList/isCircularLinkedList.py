# Time complexity: O(N)
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


    def printList(self):
        curr = self.head
        while curr:
            print(curr.data, end = ' ')
            curr = curr.next

        print()



    def isCircular(self):
        fastP = self.head

        while fastP and fastP.next and fastP.next.next:
            if fastP.next == self.head or fastP.next.next == self.head:
                return True
            fastP = fastP.next.next
       
        return False



ll = LinkedList()
ll.pushEnd(10)
ll.pushEnd(20)
ll.pushEnd(30)
ll.pushEnd(40)
ll.pushEnd(50)
ll.pushEnd(60)

ll.printList()
ll.head.next.next.next.next.next.next = ll.head
print(ll.isCircular())