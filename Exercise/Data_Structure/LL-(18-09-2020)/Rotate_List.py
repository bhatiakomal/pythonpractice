class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class LinkedList:
    def __init__(self,):
        self.head=None
    def push(self,data):
        newode=Node(data)
        newode.next=self.head
        self.head=newode
