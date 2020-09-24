#Inserting at the Head of Linked List Using Doubly Linked List
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
    def traverse(self):
        head=self.head
        while head is not None:
            print(head.data)
            head=head.nextNode
ll=LinkedList(12)
ll.insertAtHead(90)
ll.insertAtHead(100)

ll.traverse()
