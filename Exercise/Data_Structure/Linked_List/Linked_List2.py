class Node:
    def __init__(self,data):
        self.data=data
        self.nextNode=None
class Linkedlist:
    def __init__(self):
        self.head=None
        self.tail=self.head
    def makehead(self,data):
        temp=Node(data)
        if self.head==None:
            print('Linked list is empty')
            self.head=temp
            self.tail=self.head
        else:
            self.tail.nextNode=temp
            self.tail=temp
    def traverse(self):
        temp=self.head
        while temp is not None:
            print(temp.data)
            temp=temp.nextNode
ll=Linkedlist()
ll.makehead(10)
ll.makehead(20)
ll.traverse()


