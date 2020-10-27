class Node(object):
    def __init__(self,name):
        self.name=name
        self.adjacenList=[]
        self.visited=False
        self.predecessor=None
        #BFS>-queue, DFS>-stack
class deapthFirstSearch(object):
    def dfs(self,node):
        node.visited=True
        print(node.name)
        for n in node.adjacenList:
            if not n.visited:
                self.dfs(n)
node1=Node("A")
node2=Node("B")
node3=Node("C")
node4=Node("D")
node5=Node("E")
node1.adjacenList.append(node2)
node1.adjacenList.append(node3)
node2.adjacenList.append(node4)
node4.adjacenList.append(node5)
dfs=deapthFirstSearch()
dfs.dfs(node1)