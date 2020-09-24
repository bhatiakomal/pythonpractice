class Node:
    def __init__(self,data):
        self.data=data
        self.nextNode=None
class LinkedList:
    def __init__(self,value):
        self.head=Node(value)
        self.tail=self.head
    def insert(self,data):
        temp=Node(data)
        self.tail.nextNode=temp
        self.tail=temp

    def prnt(self):
        temp = self.head
        while temp is not None :
            print(temp.data)
            temp = temp.nextNode
    def length(self):
        head=self.head
        count=0
        while head:
            count+=1
            head=head.nextNode
        return count

ll=LinkedList(200)
n2=Node(300)
n3=Node(400)
n4=Node(500)
ll.head.nextNode=n2
n2.nextNode=n3
n3.nextNode=n4
ll.prnt()
print("Number of nodes:",ll.length())



