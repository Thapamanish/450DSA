# https://www.geeksforgeeks.org/intersection-of-two-sorted-linked-lists/

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


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


llist1 = Node(1)
llist1.next = Node(2)
llist1.next.next = Node(3)
llist1.next.next.next = Node(4)
llist1.next.next.next.next = Node(6)

llist2 = Node(2)
llist2.next = Node(4)
llist2.next.next = Node(6)
llist2.next.next.next = Node(8)


llist3 = intersection(llist1, llist2)

temp = llist3
while temp:
    print(temp.data, end = ' ')
    temp = temp.next
