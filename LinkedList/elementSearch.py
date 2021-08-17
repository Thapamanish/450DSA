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
        print()

    def searchElement(self, current, element):
        if current is None:
            return False

        if current.data == element:
            return True

        return self.searchElement(current.next, element)


    def searching(self, element):
        return self.searchElement(self.head, element)


ll = LinkedList()
ll.pushEnd(10)
ll.pushEnd(20)
ll.pushEnd(30)
ll.pushEnd(40)
ll.pushEnd(50)
ll.pushEnd(60)

ll.printList()

if ll.searching(60):
    print('Element found')

else:
    print('Element not found')
