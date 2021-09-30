# Question: write a program to find the intersection of two sorted linked list

# Time complexity: O(m + n) 
                  
# Auxiliary Space: O(m + n)

# intution : two pointer technique and a dummy node

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

def intersection(head1, head2):
    dummy = Node(0)
    temp = dummy

    while head1 != None and head1 != None:
        if head1.data == head2.data:
            temp.next = Node(head1.data)
            temp = temp.next
            head1 = head1.next
            head2 = head2.next

        elif head1.data < head2.data:
            head1 = head1.next

        else:
            head2  = head2.next

    return dummy.next



ll1 = LinkedList()
ll1.pushEnd(1)
ll1.pushEnd(2)
ll1.pushEnd(3)
ll1.pushEnd(4)
ll1.pushEnd(6)

ll1.printList()


ll2 = LinkedList()
ll2.pushEnd(2)
ll2.pushEnd(4)
ll2.pushEnd(6)
ll2.pushEnd(8)

ll2.printList()

ll3 = LinkedList()
ll3.head = intersection(ll1.head, ll2.head)

ll3.printList()