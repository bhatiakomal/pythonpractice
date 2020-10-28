import sys
import heapq
class Edge(object):
    def __init__(self,weight,startVertex,endVertex):
        self.weight=weight
        self.startVertex=startVertex
        self.endVertex=endVertex
class Node(object):
    def __init__(self,name):
        self.name=name
        self.visited=False
        self.predecessor=None
        self.adjacencienlist=[]
        self.minDistance=sys.maxsize
    def cmp(self, otherVertex):
        return self.__cmp__(self.minDistance,otherVertex.minDistance)
    def __lt__(self, other):
        selfPriority=self.minDistance
        otherPriority=other.minDistance
        return selfPriority<otherPriority
class Algorithm:
    def calculateShortPath(self,vertexList,startVertex):
        q=[]
        startVertex.minDistance=0
        heapq.heappush(q,startVertex)
        while len(q)>0:
            actuallVertex=heapq.heappop(q)
            for edge in actuallVertex.adjacencienlist:
                u=edge.startVertex
                v=edge.startVertex
                newDistance=u.minDistance+edge.weight
                if newDistance<v.minDistance:
                    v.predecessor=u
                    v.minDistance=newDistance
                    heapq.heappush(q,v)
    def getShortestPath(self,targetVertex):
        print("Shortest path is:",targetVertex.minDistance)
        node=targetVertex
        while node is not None:
            print(node.name)
            node=node.predecessor
node1=Node("A")
node2=Node("B")
node3=Node("C")
node4=Node("D")
node5=Node("E")
node6=Node("F")
node7=Node("G")
node8=Node("H")

edge1=Edge(5,node1,node2)
edge2=Edge(8,node1,node8)
edge3=Edge(9,node1,node5)
edge4=Edge(15,node2,node4)
edge5=Edge(12,node2,node3)

node1.adjacencienlist.append(edge1)
node1.adjacencienlist.append(edge2)
node1.adjacencienlist.append(edge3)
node2.adjacencienlist.append(edge4)
node8.adjacencienlist.append(edge5)

vertexList=(node1,node2,node3,node4,node5,node6,node7,node8)
algo=Algorithm()
algo.calculateShortPath(vertexList,node1)
algo.getShortestPath(node4)


