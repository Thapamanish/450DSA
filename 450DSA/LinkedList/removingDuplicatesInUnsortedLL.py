# Question: write a program to delete duplicate from an unsorted linked list.

# Time complexity: O(n) 
                  
# Auxiliary Space: O(n)

# intution : use a visited set to keep a track of the elements.


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

    def removeDuplicate(self):
        visited = set()
        current = self.head
        visited.add(current.data)

        while current.next:
            if current.next.data not in visited:
                visited.add(current.next.data)
                current = current.next

            else:
                current.next = current.next.next


    def printList(self):
        temp = self.head
        while temp:
            print(temp.data, end = ' ')
            temp = temp.next
        print()




ll = LinkedList()
ll.pushEnd(10)
ll.pushEnd(30)
ll.pushEnd(20)
ll.pushEnd(10)
ll.pushEnd(30)
ll.pushEnd(10)
ll.pushEnd(50)



ll.printList()

ll.removeDuplicate()

ll.printList()