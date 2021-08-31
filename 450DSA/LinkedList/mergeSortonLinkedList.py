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

    def getMiddle(self, headNode):
        if headNode is None:
            return None

        slowP = headNode
        fastP = headNode

        while fastP.next and fastP.next.next:
            slowP = slowP.next
            fastP = fastP.next.next

        return slowP

    def sortedMerge(self, left, right):
        result = None
        if left is None:
            return right
        if right is None:
            return left

        if left.data <= right.data:
            result = left
            result.next = self.sortedMerge(left.next, right)

        else:
            result = right
            result.next = self.sortedMerge(left, right.next)

        return result


    def mergeSort(self, headNode):
        if headNode is None or headNode.next is None:
            return headNode

        middle = self.getMiddle(headNode)
        middleNext = middle.next
        middle.next = None

        l = self.mergeSort(headNode)
        r = self.mergeSort(middleNext)

        sortedList = self.sortedMerge(l, r)

        return sortedList


ll = LinkedList()
ll.pushEnd(100)
ll.pushEnd(20)
ll.pushEnd(3)
ll.pushEnd(40)
ll.pushEnd(100)
ll.pushEnd(90)
ll.printList()

ll.head = ll.mergeSort(ll.head)
ll.printList()