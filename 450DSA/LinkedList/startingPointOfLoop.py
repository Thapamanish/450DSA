# Time complexity: O(N)
# Space complexity : O(1)


class Node:
    def __init__(self, data):
        self.data = data
        self.head = None



class LinkedList:
    def __init__(self):
        self.head = None



    def firstLoopNode(self):
        if not self.head or not self.head.next:
            return -1

        slowP = fastP = self.head

        while slowP and fastP and fastP.next:
            slowP = slowP.next
            fastP = fastP.next.next

            if slowP == fastP:
                slowP = self.head

                while slowP != fastP:
                    slowP = slowP.next
                    fastP = fastP.next


                return slowP.data

        return -1




ll = LinkedList()
ll.head = Node(10)
ll.head.next = Node(20)
ll.head.next.next = Node(30)
ll.head.next.next.next = Node(40)
ll.head.next.next.next.next = Node(50)


ll.head.next.next.next.next.next = ll.head.next

print(ll.firstLoopNode())
