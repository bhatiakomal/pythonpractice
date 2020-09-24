class Stack:
    def __init__(self):
        self.stake=[]
    def push(self,item):
        self.stake.append(item)
    def pop(self):
            return self.stake.pop()
    def size(self):
        if self.stake:
            return len(self.stake)
        else:
            return None
    def  isEmpty(self):
        return self.stake==[]
    def reverse(self):

    def prnt(self):
        print(self.stake)
stack=Stack()
stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)
stack.push(5)
stack.prnt()



