class Node:
    def __init__(self,data):
        self.data=data
        self.nextNode=None
class LinkedList:
    def __init__(self,value):
        self.head=Node(value)
        self.tail=self.head
    def push(self,data):
        temp=Node(data)
        self.tail.nextNode=temp
        self.tail=temp
    def deleteMid(self):
        sloptr=self.head
        fastptr=self.head
        prevNode=None
        if self.head is None:
            return
        while fastptr is not None and fastptr.nextNode is not None:
            fastptr=fastptr.nextNode.nextNode
            prevNode=sloptr
            sloptr=sloptr.nextNode
        prevNode.nextNode=sloptr.nextNode
    def prnt(self):
        temp=self.head
        while temp!=None:
            print(temp.data)
            temp=temp.nextNode
ll=LinkedList(100)
ll.push(200)
ll.push(300)
ll.push(400)
ll.push(500)
print('Before Delete Mid:')
ll.prnt()
ll.deleteMid()
print("After Delete Mid:")
ll.prnt()



