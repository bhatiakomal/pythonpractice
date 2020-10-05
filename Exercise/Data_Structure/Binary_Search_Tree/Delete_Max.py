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
def maxValueNode(node):
    current=node
    while node.right is not None:
        current=current.right
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
        temp = maxValueNode(root.left)
        root.key = temp.key
        root.left = delete(root.left, temp.key)
    return root
r=Node(50)
r=insertion(r,30)
r=insertion(r,20)
r=insertion(r,40)
r=insertion(r,70)
r=insertion(r,60)
r=insertion(r,80)
print("Insert Items are:")
inorder(r)
r=delete(r,80)
r=delete(r,20)
print('After  deletion:')
inorder(r)
