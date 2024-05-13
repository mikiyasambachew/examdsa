

class Queue:
    def __init__(self):
        self.stack1 =[]
        self.stack2=[]
    def enqueue(slef, data):
        while self.stack1:
            self.stack2.append(data)
        while self.stack2:
            self.stack1.append (self.stack2.pop())
    def peek(self):
        return self.stack1[-1]
    def dequeue(self):
        if not self.stack1:
            print(" the stack is empty,nothing to remove!")
            return -1
        return self.stack1.pop()
