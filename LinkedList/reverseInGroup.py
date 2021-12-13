# Question: write a program to reverse a linkedlist in a group

# Time complexity: O(n) 
                  
# Auxiliary Space: O(1)

# intution : just reverse the link with respective to value of k


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


    def reverseListUtil(self, current, k):
        prev = None
        while current and k>0:
            k -= 1
            temp = current.next
            current.next = prev
            prev = current
            current = temp
        return prev, current

    def reverseList(self, k):
        prev = None
        current = self.head
        while current:
            last = current

            front, current = self.reverseListUtil(current, k)

            if prev is None:
                self.head = front
            else:
                prev.next = front

            prev = last


ll = LinkedList()
ll.pushEnd(10)
ll.pushEnd(20)
ll.pushEnd(30)
ll.pushEnd(40)
ll.pushEnd(50)
ll.pushEnd(60)
ll.printList()
ll.reverseList(3)
ll.printList()
