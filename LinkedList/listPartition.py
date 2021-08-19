# https://leetcode.com/problems/partition-list/submissions/

class Node:
    def __init__(self, data = 0):
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


    def listPartition(self, x):
        small = Node()
        high = Node()
        smallHead, highHead = small, high
        current = self.head
        while current:
            if current.data < x:
                smallHead.next = current
                smallHead = smallHead.next

            else:
                highHead.next = current
                highHead = highHead.next

            current = current.next

        highHead.next = None
        smallHead.next = high.next

        return small.next



ll = LinkedList()
ll.pushEnd(1)
ll.pushEnd(4)
ll.pushEnd(2)
ll.pushEnd(3)
ll.pushEnd(5)
ll.pushEnd(2)

ll.printList()

ll.head = ll.listPartition(3)

ll.printList()

