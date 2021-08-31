# Time complexity: O(m + n)
# Space complexity : O(m + n)


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList():
    def __init__(self):
        self.head = None



def reverse(head):
    if not head or not head.next:
        return head

    curr = head
    prev = None
    while curr:
        temp = curr.next
        curr.next = prev
        prev = curr
        curr = temp

    return prev



def append(X, Y):
    X = reverse(X)
    Y = reverse(Y)
    carry = 0

    head = None
    prev = None

    while X or Y:
        newSum = 0

        if X:
            newSum += X.data

        if Y:
            newSum += Y.data

        newSum += carry


        carry = newSum // 10
        newSum = newSum % 10

        newNode = Node(newSum)
        if not head:
            head = newNode
            prev = head
        else:
            prev.next = newNode
            prev = prev.next


        X = X.next if X else X
        Y = Y.next if Y else Y

    if carry:
        prev.next = Node(carry)

    head = reverse(head)
    printList(head)
    


def printList(head):
    curr = head
    while curr:
        print(curr.data, end = ' ')
        curr = curr.next

    print()


lList1 = LinkedList()
lList1.head = Node(1)
lList1.head.next = Node(2)
lList1.head.next.next = Node(3)
printList(lList1.head)



lList2 = LinkedList()
lList2.head = Node(9)
lList2.head.next = Node(9)
lList2.head.next.next = Node(9)
printList(lList2.head)

append(lList1.head, lList2.head)






            