# Time Complexity : O(N)
# Space Complexity : O(1)


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None


    def reverseList(self):
        curr = self.head
        prev = None
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        self.head = prev



    def addDigit(self, digit):
        if not self.head:
            return 
        self.reverseList()
        carry = digit
        curr = self.head

        while carry:
            newSum = curr.data + carry

            curr.data = newSum % 10
            carry = newSum // 10

            if not curr.next:
                break

            curr = curr.next

        if carry > 0:
            curr.next = Node(carry)

        self.reverseList()


    def printList(self):
        curr = self.head
        while curr:
            print(curr.data, end = ' ')
            curr = curr.next

        print()



ll = LinkedList()
ll.head = Node(9)
ll.head.next = Node(9)
ll.head.next.next = Node(9)
ll.head.next.next.next = Node(9)
ll.printList()
ll.addDigit(1)
ll.printList()

