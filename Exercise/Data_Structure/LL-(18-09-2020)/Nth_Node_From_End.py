class Node:
    def __init__(self,data):
        self.data=data
        self.nextNode=None
class LinkedList:
    def __init__(self):
        self.head = None
    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node
    def printNthNode(self,n):
        temp=self.head
        length=0
        while temp!=None:
            temp=temp.nextNode
            length+=1
        if n>length:
            print("Not exists")
            return
        temp=self.head
        for i in range(0,length-n):
            tem=temp.nextNode
        print(temp.data)
ll=LinkedList()
ll.push(12)
ll.push(23)
ll.push(76)
ll.push(89)
ll.printNthNode(1)