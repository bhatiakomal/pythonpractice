class Queue:
    def __init__(self):
        self.queue=[]
    def isEmpty(self):
        return self.queue==[]
    def enqueue(self,data):
        self.queue.append(data)
    def dequeue(self):
        data=self.queue[0]
        del self.queue[0]
        return data
    def peek(self):
        return self.queue[0]
    def size(self):
        return len(self.queue)
queue=Queue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
queue.enqueue(4)
queue.enqueue(5)
print('size of queue:',queue.size())
print('remove item',queue.dequeue())
print('size of queue:',queue.size())