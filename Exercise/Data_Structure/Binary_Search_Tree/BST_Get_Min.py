class Node:
    def __init__(self,data,parent):
        self.data=data
        self.rightChild=None
        self.leftChild=None
        self.parent=parent
class BinarySearchTree:
    def __init__(self):
        self.root=None
    def insert(self,data):
        if self.root is None:
            self.root=Node(data,None)
        else:
            self.insert_node(data,self.root)
    def insert_node(self,data,node):
        if data <node.data:
            if node.leftChild is not None:
                self.insert_node(data,node.leftChild)
            else:
                node.leftChild=Node(data,node)
        else:
            if node.rightChild is not None:
                self.insert_node(data,node.rightChild)
            else:
                node.rightChild=Node(data,node)
    def get_min_value(self):
        if self.root is not None:
            return self.get_min(self.root)
    def get_min(self,node):
        if node.leftChild is not None:
            return self.get_min(node.leftChild)
        return node.data
    def traverse(self):
        if self.root is not None:
            self.traverse_in_order(self.root)
    def traverse_in_order(self,node):
        if node.leftChild is not None:
            self.traverse_in_order(node.leftChild)
        print(node.data)
        if node.rightChild is not None:
            self.traverse_in_order(node.rightChild)
bst=BinarySearchTree()
bst.insert(12)
bst.insert(-12)
bst.insert(15)
bst.insert(2)


bst.insert(29)
bst.insert(100)
bst.traverse()
print("Min item:",bst.get_min(bst.root))
