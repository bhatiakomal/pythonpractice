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
    def prnt(self):
        temp=self.head
        while temp is not None:
            print(temp.data)
            temp=temp.nextNode

    def middleElement(self):
        fastPointer = self.head
        slowPointer = self.head
        prev=None
        while fastPointer is not None and fastPointer.nextNode is not None:
            fastPointer = fastPointer.nextNode.nextNode
            prev = slowPointer
            slowPointer = slowPointer.nextNode
        prev.nextNode=slowPointer.nextNode
ll=LinkedList(1000)
ll.insert(12)
ll.insert(23)
ll.insert(76)
ll.insert(89)
ll.prnt()
print('After middle delete')
ll.middleElement()
ll.prnt()
