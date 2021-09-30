# Question: write a program to find the starting point of loop in a linked list

# Time complexity: O(n) 
                  
# Auxiliary Space: O(1)

# intution : checks for the loop using Floyd’s Cycle-Finding Algorithm

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


                return fastP.data

        return -1




ll = LinkedList()
ll.pushEnd(10)
ll.pushEnd(20)
ll.pushEnd(30)
ll.pushEnd(40)
ll.pushEnd(50)


ll.head.next.next.next.next.next = ll.head.next.next

print(ll.firstLoopNode())
