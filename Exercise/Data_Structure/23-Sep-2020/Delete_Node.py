class Node:
    def __init__(self,data):
        self.data=data
        self.nextNode=None
class LinkedList:
    def __init__(self,value):
        self.head=Node(value)
        self.tail=self.head
    def push(self,data):
        temp=Node(data)
        self.tail.nextNode=temp
        self.tail=temp
    def deleteNode(self,data):
        temp=self.head
        while temp is not None:
            if (temp.data==data):
                break
            prev=temp
            temp=temp.nextNode
        prev.nextNode = temp.nextNode
    def prnt(self):
        temp=self.head
        while temp!=None:
            print(temp.data)
            temp=temp.nextNode

ll=LinkedList(100)
ll.push(200)
ll.push(300)
ll.push(400)
ll.push(500)
ll.prnt()
ll.deleteNode(300)
print("Afetr Delete Node:")
ll.prnt()

