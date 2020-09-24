#Add Node between two nodes
class  Node:
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
      
    def insertBetween(self,priviousNode,newdata):
        if priviousNode is None:
            print("Privious node is empty")
        newNode=Node(newdata)
        newNode.nextNode=priviousNode.nextNode
        priviousNode.nextNode=newNode
    def prnt(self):
        temp=self.head
        while temp is not None:
            print(temp.data)
            temp=temp.nextNode
ll=LinkedList(10)
ll.head=Node('A')
n2=Node("B")
n3=Node("C")
n4=Node("D")
ll.head.nextNode=n2
n2.nextNode=n3
n3.nextNode=n4
ll.insertBetween(ll.head.nextNode,"E")
ll.prnt()

