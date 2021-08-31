# Time Complexity : O(m + n)
# Space Complexity : O(1)

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def getCount(head):
    count = 0
    while head:
        count += 1
        head = head.next
    return count

def getIntersectionPointUtil(d, head1, head2):
    curr1 = head1
    curr2 = head2

    for i in range(d):
        if not curr1:
            return -1
        curr1 = curr1.next
    curr1 = curr1.next
    curr2 = curr2.next

    while curr1 and curr2:
        if curr1 == curr2:
            return curr1.data

        curr1 = curr1.next
        curr2 = curr2.next

    return -1



def getIntersectionPoint(head1, head2):
    c1 = getCount(head1)
    c2 = getCount(head2)
    if c1 > c2:
        return getIntersectionPointUtil(c1 - c2, head1, head2)
    else:
        return getIntersectionPointUtil(c2 - c1, head2, head1)



common=Node(15)


head1=Node(3)
head1.next=Node(6)
head1.next.next=Node(9)
head1.next.next.next=common
head1.next.next.next.next=Node(30)


head2=Node(10)
head2.next=common
head2.next.next=Node(30)

print("The node of intersection is ",getIntersectionPoint(head1,head2))