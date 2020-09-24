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
    def length(self):
        temp=self.head
        count=0
        while (temp):
            count+=1
            temp=temp.nextNode
        return count
ll=LinkedList()
ll.push(200)
ll.push(300)
ll.push(400)
ll.push(500)
print('Lenght:',ll.length())

