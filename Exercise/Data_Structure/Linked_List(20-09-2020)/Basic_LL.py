class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self,value):
        self.head = Node(value)
        self.tail = self.head

    def insert(self,data):
        temp = Node(data)
        self.tail.next =temp
        self.tail = temp

    def prnt(self):
        temp=self.head
        while temp!=None:
            print(temp.data)
            temp=temp.next
ll=LinkedList(100)
ll.insert(90)
ll.insert(80)
ll.prnt()

