class Node:
    def __init__(self,data):
        self.data=data
        self.nextNode=None
        self.prevNode=None
class LinkedList:
    def __init__(self,value):
        self.head=Node(value)
        self.tail=self.head
    def insertAtHead(self,data):
        newNode = Node(data)
        newNode.nextNode=self.head
        newNode.prevNode=None
        self.head=newNode
    def insertAfter(self,prevNode,data):
        newNode=Node(data)
        newNode.nextNode=prevNode.nextNode
        prevNode.nextNode=newNode
        newNode.prevNode=prevNode
        if newNode.nextNode is not None:
            newNode.nextNode.prevNode=newNode
    def traverse(self):
        head=self.head
        while head is not None:
            print(head.data)
            head=head.nextNode
ll=LinkedList(12)
ll.insertAtHead(90)
ll.insertAtHead(20)
ll.insertAfter(ll.head.nextNode,9)
ll.traverse()