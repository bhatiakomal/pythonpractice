class Stack:
    def __init__(self):
        self.item=[]
    def push(self,item):
        self.item.append(item)
    def pop(self):
            return self.item.pop()
    def size(self):
        if self.item:
            return len(self.item)
        else:
            return None
    def  isEmpty(self):
        return self.item==[]
def reverse(str):
    TemStr=''
    stack=Stack()
    for i in range(len(str)):
        stack.push(str[i])
    while not stack.isEmpty():
        Tem=stack.pop()
        TemStr=TemStr+Tem
    return TemStr
if __name__=="__main__":
    print(reverse('Komolika'))