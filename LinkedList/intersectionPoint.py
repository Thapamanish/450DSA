# Question: write a program to find the intersection point

# Time complexity: O(m + m) i.e. m -> length of longest linked list 
                  
# Auxiliary Space: O(1)

# intution : use two pointer technique

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None



def printList(head):
    current = head
    while current:
        print(current.data, end = ' ')
        current = current.next

    print()



def getIntersectionPoint(head1, head2):
    if not head1 or not head2:
        return None

    A = head1
    B = head2

    while A != B:
        if A:
            A = A.next
        else:
            A = head2

        if B:
            B = B.next
        else:
            B = head1

    return A.data if A else None



common=Node(90)
common.next = Node(30)



head1=Node(3)
head1.next=Node(6)
head1.next.next=Node(9)
head1.next.next.next=common
printList(head1)


head2=Node(10)
head2.next = Node(40)
head2.next.next=common
printList(head2)


print("The node of intersection is ",getIntersectionPoint(head1,head2))