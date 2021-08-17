

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def pushFront(self, data):
        newNode = Node(data)
        newNode.next = self.head
        self.head = newNode


    def printLinkedList(self):
        current = self.head
        while current:
            print(current.data, end = ' ')
            current = current.next

        print()

    def insertAfter(self,targetNode, data):
        current = self.head
        newNode = Node(data)
        while current:
            if current.data == targetNode:
                newNode.next = current.next
                current.next = newNode
                break

            current = current.next

        if current is None:
            print('check the target node')

    def insertBefore(self, targetNode, data):
        newNode = Node(data)
        if self.head.data == targetNode:
            newNode.next = head
            head = newNode
        
        prev = self.head
        current = self.head.next 
        while current:
            if current.data == targetNode:
                newNode.next = prev.next
                prev.next = newNode
                break

            prev = current
            current = current.next


        if current is None:
            print('Check the target node')


    def insertEnd(self, data):
        newNode = Node(data)
        if self.head is None:
            self.head = newnode
            return 
        current = self.head
        while current.next:
            current = current.next
        current.next = newNode


    def deleteNode(self, targetNode):
        temp = self.head
        if temp is not None:
            if temp.data == targetNode:
                self.head = temp.next
                return 


        current = self.head.next
        prev = self.head

        while current:
            if current.data == targetNode:
                prev.next = current.next
                return 

            prev = current
            current = current.next


    def delPosNode(self, targetNode):
        i = 0
        if targetNode == i:
            self.head = self.head.next
            return

        current = self.head.next
        prev = self.head

        while current:
            i += 1
            if i == targetNode:
                prev.next = current.next
                return

            prev = current
            current = current.next


        if current is None:
            print('check the position')







ll = LinkedList()
ll.head = Node(10)
ll.pushFront(20)
ll.pushFront(30)
ll.pushFront(40)
ll.printLinkedList()
ll.insertAfter(10, 60)
ll.printLinkedList()
ll.insertBefore(60, 90)
ll.printLinkedList()
ll.insertEnd(80)
ll.printLinkedList()
ll.deleteNode(40)
ll.printLinkedList()
ll.delPosNode(1)
ll.printLinkedList()
