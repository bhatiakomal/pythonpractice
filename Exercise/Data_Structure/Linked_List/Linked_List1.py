class Node:
    def __init__(self,data):
        self.data=data
        self.nextNode=None
class LinkedList:
    def __init__(self,value):
        self.head=Node(value)
        self.tail=self.head
    def insert(self,data):
        temp=self.head
        self.tail.nextNode=temp
        self.tail=temp
    def traverse(self):
        temp=self.head
        while temp is not None:
            print(temp.data)
            temp=temp.nextNode
ll=LinkedList(100)
ll.traverse()