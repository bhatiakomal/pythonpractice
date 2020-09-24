class Node:
    def __init__(self,data):
        self.data=data
        self.nextNode=None
class LinkedList:
    def __init__(self):
        self.head=None
        self.tail=self.head
    def makeHead(self,data):
        temp=Node(data)
        if self.head is None:
            print("Your Linked List is empty")
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
ll=LinkedList()
ll.makeHead(10)
ll.makeHead(20)
ll.traverse()

