# Time Complexity : O(N)
# Space Complexity : O(1)


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None


    def removeDuplicate(self):
        visited = set()
        temp = self.head
        visited.add(temp.data)

        while temp.next:
            if temp.next.data not in visited:
                visited.add(temp.next.data)
                temp = temp.next
            else:
                temp.next = temp.next.next


    def printList(self):
        temp = self.head
        while temp:
            print(temp.data, end = ' ')
            temp = temp.next
        print()




ll = LinkedList()
ll.head = Node(10)
ll.head.next = Node(30)
ll.head.next.next = Node(20)
ll.head.next.next.next = Node(10)
ll.head.next.next.next.next = Node(30)
ll.head.next.next.next.next.next = Node(10)
ll.head.next.next.next.next.next.next = Node(50)


ll.printList()

ll.removeDuplicate()

ll.printList()