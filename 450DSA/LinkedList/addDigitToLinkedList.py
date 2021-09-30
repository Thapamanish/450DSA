# Question: write a program to add a digit to a linked list

# Time complexity: O(n) 
                  
# Auxiliary Space: O(1)

# intution : reverse the list and do a simple addition using carry concept
            # and reverse the list back

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


    def reverseList(self):
        current = self.head
        prev = None
        while current:
            temp = current.next
            current.next = prev
            prev = current
            current = temp

        self.head = prev



    def addDigit(self, digit):
        if not self.head:
            return 
        self.reverseList()
        carry = digit
        current = self.head

        while carry:
            newSum = current.data + carry

            current.data = newSum % 10
            carry = newSum // 10

            if not current.next:
                break

            current = current.next

        if carry > 0:
            current.next = Node(carry)

        self.reverseList()



    def printList(self):
        current = self.head
        while current:
            print(current.data, end = ' ')
            current = current.next

        print()



ll = LinkedList()
ll.pushEnd(9)
ll.pushEnd(9)
ll.pushEnd(9)
ll.pushEnd(9)

ll.printList()
ll.addDigit(1)
ll.printList()

