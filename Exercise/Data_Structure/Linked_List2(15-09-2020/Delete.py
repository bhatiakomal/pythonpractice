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
    def deleteNode(self,data):
        temp=self.head
        while temp is not None:
            if (temp.data==data):
                break
            prev=temp
            temp=temp.nextNode
        prev.nextNode = temp.nextNode

    def traverse(self):
        head = self.head
        while head is not None:
            print(head.data)
            head=head.nextNode
ll=LinkedList('Anu')
ll.insert("Priya")
ll.insert("Arti")
ll.insert("Komal")
ll.insert("Jyoti")
ll.traverse()
print("After removing Node")
ll.deleteNode('Priya')
ll.traverse()

