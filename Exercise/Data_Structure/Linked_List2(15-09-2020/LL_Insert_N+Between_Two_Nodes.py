class Node:
    def  __init__(self,data):
        self.data=data
        self.next=None
class Linked:
    def  __init__(self,value):
        self.head=Node(value)
        self.tail=self.head
    def insert(self,data):
        newNode=Node(data)
        self.tail.next=newNode
        self.tail=newNode
    def prnt(self):
        head=self.head
        while  head is not None:
            print(head.data)
            head=head.next
    def insertBetweenTwo(self,priviousNode,newData):
        if priviousNode is None:
            print("Can not be insert:")
        newNode=Node(newData)
        newNode.next=priviousNode.next
        priviousNode.next=newNode
ll=Linked(900)
n2=Node(2121)
n3=Node(800)
n4=Node(567)
ll.head.next=n3
n2.next=n3
n3.next=n4
ll.insertBetweenTwo(ll.head.next,400)
ll.prnt()