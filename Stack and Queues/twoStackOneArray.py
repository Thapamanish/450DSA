class Stack:
    def __init__(self, n):
        self.s = [None] * n
        self.top1 = -1
        self.top2 = n
        self.capacity = n
     

    def push1(self, data):
        if self.top1 + 1 == self.top2:
            print('stack is full')
            return

        self.top1 += 1
        self.s[self.top1] = data


    def push2(self, data):
        if self.top1 + 1 == self.top2:
            print('stack is full')
            return

        self.top2 -= 1
        self.s[self.top2] = data


    def pop1(self):
        if self.top1 == -1:
            return 'stack 2 is empty'


        x = self.s[self.top1]
        self.top1 -= 1
        return x


    def pop2(self):
        if self.top2 == self.capacity:
            return 'stack 2 is empty'

        
        x = self.s[self.top2]
        self.top2 += 1
        return x


s = Stack(5)
s.push1(10)
s.push1(20)
s.push1(30)

s.push2(70)
s.push2(80)
s.push2(90)

print(s.pop1())
print(s.pop1())

print(s.pop2())
print(s.pop2())
print(s.pop2())