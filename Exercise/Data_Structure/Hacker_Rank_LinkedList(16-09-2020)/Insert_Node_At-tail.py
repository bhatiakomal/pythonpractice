class Node:
    def __init__(self,data):
        self.data=data
        self.nextNode=None
class LinkedList:
    def __init__(self,value):
        self.head=Node(value)
        self.tail=self.head
    def insert(self,data):
        newNode=Node(data)
        self.tail.nextNode=newNode
        self.tail=newNode
    def traverse(self):
        head=self.head
        while head is not None:
            print(head.data)
            head=head.nextNode
ll=LinkedList(100)
ll.insert(20)
ll.insert(30)
ll.insert(40)
ll.traverse()
