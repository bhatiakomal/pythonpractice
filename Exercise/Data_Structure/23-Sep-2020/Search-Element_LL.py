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
    def search(self,item):
        temp=self.head
        while temp!=None:
            if temp.data==item:
                return True
            temp=temp.nextNode
        return False
ll=LinkedList()
ll.push(200)
ll.push(300)
ll.push(400)
ll.push(500)
if ll.search(500):
    print("Yes")
else:
    print("Noo")