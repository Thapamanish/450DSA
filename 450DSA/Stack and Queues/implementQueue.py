class Queue:
    def __init__(self, n):
        self.q = [None] * n
        self.front = 0
        self.rear = -1
        self.capacity = n
        self.count = 0

    def enqueue(self, data):
        if self.count == self.capacity:
            print('Queue is full')
            return 

        self.rear = (self.rear + 1) % self.capacity
        self.q[self.rear] = data
        self.count += 1


    def dequeue(self):
        if self.count == 0:
            print('Queue is empty')
            return 

        self.front = (self.front + 1) % self.capacity
        self.count -= 1

    def peek(self):
        if self.count == 0:
            print('Queue is empty')
            return

        return self.q[self.front]



q = Queue(5)
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
q.enqueue(40)
q.enqueue(50)
q.enqueue(60)
print(q.peek())
q.dequeue()
print(q.peek())
q.enqueue(60)
q.dequeue()
q.dequeue()
q.dequeue()
q.dequeue()
q.dequeue()
q.dequeue()
