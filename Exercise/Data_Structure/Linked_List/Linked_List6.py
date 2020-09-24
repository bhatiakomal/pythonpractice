class Node:
    def __init__(self,data):
        self.data=data
        self.nextNode=0
class LinkedList:
    def __init__(self,value):
        self.head=Node(value)
        self.tail=self.head
    def insertStart(self,data):
        temp=Node(data)
        temp.nextNode=self.head
        self.head=temp
    def prnt(self):
        temp = self.head
        while temp is not None:
            print(temp.data)
            temp = temp.nextNode
ll=LinkedList(12)
ll.insertStart(14)
ll.prnt()