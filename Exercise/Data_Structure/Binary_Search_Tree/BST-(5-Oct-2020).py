class Node:
    def __init__(self,key):
        self.right=None
        self.left=None
        self.val=key
def insertion(root,key):
    if root is None:
        return Node(key)
    else:
        if  root.val==key:
            return root
        elif root.val<key:
            root.right=insertion(root.right,key)
        else:
            root.left = insertion(root.left, key)
    return root
def inorder(root):
    if root:
        inorder(root.left)
        print(root.val)
        inorder(root.right)
r=Node(50)
r=insertion(r,90)
r=insertion(r,00)
r=insertion(r,100)
r=insertion(r,43)
r=insertion(r,1000)
inorder(r)