class Node:
    def __init__(self,data):
        self.data=data
        self.nextNode=None
class LinkedList:
    def __init__(self,value):
        self.head=Node(value)
        self.tail=self.head

    def insert(self, data):
        temp = Node(data)
        self.tail.nextNode = temp
        self.tail = temp
    def printMiddle(self):
        fastpointer=self.head
        slowptr=self.head
        if self.head is not None:
            while fastpointer is not None and  fastpointer.nextNode is not None:
                fastpointer=fastpointer.nextNode.nextNode
                slowptr=slowptr.nextNode
            print('Middle Element:',slowptr.data)
    def prnt(self):
        temp=self.head
        while temp!=None:
            print(temp.data)
            temp=temp.nextNode
ll=LinkedList(100)
ll.insert(200)
ll.insert(300)
ll.insert(400)
ll.insert(500)
ll.insert(600)
ll.prnt()
ll.printMiddle()

