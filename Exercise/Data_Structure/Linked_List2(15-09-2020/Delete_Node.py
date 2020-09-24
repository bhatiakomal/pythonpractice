#Removal of head
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
    def removehead(self,data):
        temp=self.head
        if (temp is not None):
            if (temp.data==data):
                self.head=temp.nextNode
                temp=None
                return
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
ll.removehead("Komal")
print(">>>>")
ll.traverse()