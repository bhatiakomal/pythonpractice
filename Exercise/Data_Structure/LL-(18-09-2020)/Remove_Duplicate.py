class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class LinkedList:
    def __init__(self):
        self.head=None
    def insert(self,value):
        newNode=Node(value)
        newNode.next=self.head
        self.head=newNode
    def printList(self):
        temp = self.head
        while (temp):
            print(temp.data)
            temp = temp.next
    def removeDuplicates(self):
        temp = self.head
        if temp is None:
            return
        while temp.next is not  None:
            if temp.data == temp.next.data:
                new = temp.next.next
                temp.next=None
                temp.next=new
            else:
                temp = temp.next
        return self.head

ll = LinkedList()
ll.insert(12)
ll.insert(15)
ll.insert(12)
ll.insert(16)
print("Original List is:")
ll.printList()
print("After removing duplicates")
ll.removeDuplicates()
ll.printList()

