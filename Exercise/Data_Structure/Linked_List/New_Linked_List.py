class Node:
    def __init__(self,data):
        self.data=data
        self.nextNode=None
class LinkedList:
    def __init__(self):
        self.head=None
        self.tail=self.head
    def makehead(self,data):
        temp = Node(data)
        if self.head==None:
            print("LL is empty")
            self.head=temp
            self.tail=self.head
        else:
            self.tail.nextNode=temp
            self.tail=temp
ll=LinkedList()
ll.makehead()




ll=LinkedList()
ll.makehead()