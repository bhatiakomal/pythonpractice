class Node(object):
    def __init__(self,name):
        self.name=name
        self.adjacenList=[]
        self.visited=False
        self.predecessor=None
class BreadthFirstSearch:
    def bfs(self,startNode):
        queue=[]
        queue.append(startNode)
        startNode.visited=True
        while queue:
        #While queue is not empty
            actualNode=queue.pop(0)
            print(actualNode.name)
            for n in actualNode.adjacenList:
                if not n.visited:
                    n.visited=True
                    queue.append(n)
node1=Node("A")
node2=Node("B")
node3=Node("C")
node4=Node("D")
node5=Node("E")
node1.adjacenList.append(node2)
node1.adjacenList.append(node3)
node2.adjacenList.append(node4)
node4.adjacenList.append(node5)
bfs=BreadthFirstSearch()
bfs.bfs(node1)
