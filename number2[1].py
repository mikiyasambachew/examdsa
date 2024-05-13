class stack:
    def __init__(self):
        self.stack =[]
        def push(self, val):
            self.stack.append(val)
        def pop(self):
            if len(self.stack) <= 0:
                print("empty stack!")
                return
            return self .stack.pop()
        def peek(self):
            return self.stack[-1]
        def getsize(self):
            return len(self.stack)