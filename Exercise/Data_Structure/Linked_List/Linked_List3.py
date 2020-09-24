#print middle of the print List
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
        head=self.head
        while head is not None:
            print(head.data)
            head=head.nextNode
    def lengthOfLL(self):
        temp=self.head
        count=0
        while (temp):
            count+=1
            temp=temp.nextNode
        return count

ll=LinkedList(10)
ll.insert(20)
ll.insert(30)
ll.insert(40)
ll.insert(50)
ll.prnt()
print('length:',ll.lengthOfLL())
