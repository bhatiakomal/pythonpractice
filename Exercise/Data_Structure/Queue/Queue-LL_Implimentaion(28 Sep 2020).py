class Node:
    def __init__(self,data):
        self.data=data
        self.nextNode=None
class Queue:
    def __init__(self):
        self.head=self.tail=None
    def isEmpty(self):
        return self.head==None
    def enQueue(self,item):
        temp=Node(item)
        if self.tail==None:
            self.head=self.tail=temp
            return
        self.tail.nextNode=temp
        self.tail=temp
    def deQueue(self):
        if self.isEmpty():
            return
        temp=self.head
        self.head=temp.nextNode
        if (self.head==None):
            self.tail=None
if __name__== '__main__':
    q = Queue()
    q.enQueue(10)
    q.enQueue(20)
    q.deQueue()
    q.enQueue(30)
    q.enQueue(40)
    q.enQueue(50)
    q.deQueue()
    print("Queue Front " + str(q.head.data))
    print("Queue Rear " + str(q.tail.data))
