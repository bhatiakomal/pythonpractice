class Node:
    def __init__(self,data):
        self.data=data
        self.nextNode=None
class LinkedList:
    def __init__(self,value):
        self.head=Node(value)
        self.tail=self.head
    def insert(self,data):
        temp=Node(data)
        self.tail.nextNode=temp
        self.tail=temp
ll=LinkedList(89)
ll.insert(20)


