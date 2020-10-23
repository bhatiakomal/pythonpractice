class Node:
    def __init__(self,character):
        self.character=character
        self.leftNode=None
        self.rightNode=None
        self.middleNode=None
        self.value=0
class TST(object):
    def __init__(self):
        self.rootNode=None
    def put(self,key,value):
        self.rootNode=self.putitem(self.rootNode,key,value,0)
    def putitem(self,node,key,value,index):
        c=key[index]
        if node==None:
            node=Node(c)
        if c<node.character:
            node.leftNode=self.putitem(node.leftNode,key,value,index)
        elif c>node.character:
            node.rightNode=self.putitem(node.rightNode,key,value,index)
        elif index<len(key)-1:
            node.middleNode=self.putitem(node.middleNode,key,value,index+1)
        else:
            node.value=value
        return node
    def get(self,key):
        node=self.getitem(self.rootNode,key,0)
        if node==None:
            return -1
        return node.value
    def getitem(self,node,key,index):
        if node==None:
            return None
        c=key[index]
        if c<node.character:
            return self.getitem(node.leftNode,key,index)
        elif c>node.character:
            return self.getitem(node.rightNode,key,index)
        elif index<len(key)-1:
            return self.getitem(node.middleNode,key,index+1)
        else:
            return node
tst=TST()
tst.put("Horse",200000)
tst.put("Cow",30000)
tst.put("Dog",1500)
print(tst.get("Horse"))


