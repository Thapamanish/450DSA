# https://practice.geeksforgeeks.org/problems/detect-loop-in-linked-list/1/?company[]=Lybrate&company[]=Lybrate&page=1&query=company[]Lybratepage1company[]Lybrate#


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
 
 
class LinkedList:
    def __init__(self):
        self.head = None

    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def printList(self):
        temp = self.head
        while(temp):
            print(temp.data, end = " ")
            temp = temp.next
 
    def detectLoop(self):
        slow_p = self.head
        fast_p = self.head
        while(slow_p and fast_p and fast_p.next):
            slow_p = slow_p.next
            fast_p = fast_p.next.next
            if slow_p == fast_p:
                return True
 
 

llist = LinkedList()
llist.push(20)
llist.push(4)
llist.push(15)
llist.push(10)
 
llist.printList()
llist.head.next.next.next.next = llist.head

if(llist.detectLoop()):
    print ("Found Loop")
else:
    print ("No Loop")