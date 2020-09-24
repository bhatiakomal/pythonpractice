class Stack:
    def __init__(self):
        self.stack=[]
    #for insert items
    def push(self,data):
        self.stack.append(data)

    #for remove item
    def pop(self):
        data=self.stack[-1]
        del self.stack[-1]
        return data
    #retrun last item without removing it
    def peek(self):
        return self.stack[-1]
    def size(self):
        return len(self.stack)
stack=Stack()
stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)
stack.push(5)
print('size of stack:',stack.size())
print('Popped item:',stack.pop())
print('size of stack:',stack.size())
print('Peak item:',stack.peek())
print('size of stack:',stack.size())