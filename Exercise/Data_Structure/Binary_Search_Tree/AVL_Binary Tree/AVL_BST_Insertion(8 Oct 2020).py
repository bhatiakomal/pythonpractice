class Node:
    def __init__(self,val):
        self.val=val
        self.right=None
        self.left=None
        self.height=1
class AVL_Tree:
    def insert(self,root,key):
        if not root:
            return Node(key)
        elif key<root.val:
            root.left=self.insert(root.left,key)
        else:
            root.right=self.insert(root.right,key)
        #Get Height
        root.height=1+max(self.getHeight(root.left),self.getHeight(root.right))
        #Balance Node
        balance=self.getBalance(root)
        #LL Rotation
        if balance>1 and key<root.left.val:
            return self.rightRotate(root)
        #RR Rotation
        if balance<-1 and key>root.right.val:
            return self.leftRotate(root)
        #LR-LL Rotation
        if balance>1 and key>root.left.val:
            root.left=self.leftRotate(root.left)
            return self.rightRotate(root)
        #RL-RR Rotation
        if balance<-1 and key<root.right.val:
            root.right=self.rightRotate(root.right)
            return self.leftRotate(root)
        return root
    def getHeight(self,root):
        if not root:
            return 0
        return root.height
    def getBalance(self,root):
        if not root:
            return 0
        return self.getHeight(root.left)-self.getHeight(root.right)
    def leftRotate(self,z):
        y=z.right
        T2=y.left
        #Make Rotations
        y.left=z
        z.right=T2
        z.height=1+max(self.getHeight(z.left),self.getHeight(z.right))
        y.height=1+max(self.getHeight(y.left),self.getHeight(y.right))
        return y
    def rightRotate(self,z):
        y=z.left
        T3=y.right
        #Make Rotations
        y.right=z
        z.left=T3
        z.height=1+max(self.getHeight(z.left),self.getHeight(z.right))
        y.height=1+max(self.getHeight(y.left),self.getHeight(y.right))
        return y
    def traversal(self,root):
        if not root:
            return
        print('{0}'.format(root.val),end=" ")
        self.traversal(root.left)
        self.traversal(root.right)
tree=AVL_Tree()
root=None
root=tree.insert(root,10)
root=tree.insert(root,20)
root=tree.insert(root,30)
root=tree.insert(root,40)
root=tree.insert(root,50)
tree.traversal(root)

