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
    def length(self):
        temp=self.head
        count=0
        while temp:
            count+=1
            temp=temp.nextNode
        return count
    def traverse(self):
        head = self.head
        while head is not None:
            print(head.data)
            head=head.nextNode

ll=LinkedList('pray')
ll.insert(20)
ll.insert("Komolika")
ll.insert(40)
ll.insert(50.23)
ll.traverse()
print('Length of Linked List:',ll.length())