class Node:
    def __init__(self,key):
        self.right=None
        self.left=None
        self.key=key
def insertion(node,key):
    if node is None:
        return Node(key)
    else:
        if node.key<key:
            node.right=insertion(node.right,key)
        else:
            node.left = insertion(node.left, key)
    return node
def inorder(root):
    if root:
        inorder(root.left)
        print(root.key)
        inorder(root.right)
def minValueNode(node):
    current=node
    while node.left is not None:
        current=current.left
    return current
def delete(root,key):
    if root  is None:
        return root
    if key <root.key:
        root.left=delete(root.left,key)
    elif (key>root.key):
        root.right=delete(root.right,key)
    else:
        if root.left is None:
            temp=root.right
            root=None
            return root
        elif root.right is None:
            temp = root.left
            root = None
            return temp
        temp = minValueNode(root.right)
        root.key = temp.key
        root.right = delete(root.right, temp.key)
    return root
r=Node(50)
r=insertion(r,90)
r=insertion(r,00)
r=insertion(r,100)
r=insertion(r,43)
r=insertion(r,1000)
print("Insert Items are:")
inorder(r)
r=delete(r,1000)
print('After  deletion:')
inorder(r)
