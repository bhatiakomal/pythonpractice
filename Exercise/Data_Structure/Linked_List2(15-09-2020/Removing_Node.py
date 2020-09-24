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
    def removal(self,data):
        if self.head is None:
            return
        temp=self.head
        priviousNode=None
        while temp is not None and temp.data!=data:
            priviousNode=temp
            temp=temp.nextNode
        if temp is None:
            return
        #Remove Head
        if priviousNode is None:
            self.head=temp.nextNode
        else:
            self.head=temp.nextNode
    def traverse(self):
        head=self.head
        while head is not None:
            print(head.data)
            head=head.nextNode
ll=LinkedList('Komal')
ll.insert(12)
ll.insert(13)
ll.insert(14)
ll.insert(15)
ll.traverse()
ll.removal("Komal")
print(">>>>")
ll.traverse()