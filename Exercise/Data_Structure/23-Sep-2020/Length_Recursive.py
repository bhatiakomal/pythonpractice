class Node:
    def __init__(self,data):
        self.data=data
        self.nextNode=None
class LinkedList:
    def __init__(self):
        self.head=None
    def push(self,data):
        newNode=Node(data)
        newNode.nextNode=self.head
        self.head=newNode
    def length(self,node):
        temp=self.head
        if not node:
            return 0
        else:
            return 1+self.length(node.nextNode)
    def getLength(self):
        return self.length(self.head)
ll=LinkedList()
ll.push(200)
ll.push(300)
ll.push(400)
ll.push(500)
print('Lenght:',ll.getLength())
