from Vertex import Vertex
from Edge import Edge
from MinHeap import MinHeap
from Tree import Tree

class MinimumSpanning:

    def __init__(self, vertices, edges, startNode, hasBoard):
        self.vertices = vertices
        self.edges = edges
        self.startNode = startNode
        self.minHeap = MinHeap()
        self.hasBoard = hasBoard.lower() == "y"
        self.primRunEdges = []

    # Get all edges adjecent to a list of vertices
    def primEdges(self, visited):
        edges = []
        for vertex in visited:
            neighbors = self.getEdgesFromVertex(vertex)
            for edge in neighbors:
                edges.append(edge)
        return edges

    # gets all of the edges adjacent to the given vertex
    def getEdgesFromVertex(self, vertex):
        adjEdges = []
        for e in self.edges:
            if e.l1 == vertex.label:
                adjEdges.append(e)
        return adjEdges

    # get vertex from given label
    def findByLabel(self, label):
        if label:
            for v in self.vertices:
                if v.label == label:
                    return v

    # run prims from preorder traversal
    def primsAlgorithm(self):
        # set initial distance to inf
        for vertex in self.vertices:
            vertex.dist = 1000000
        self.startNode.dist = 0
        # create tree for traversal
        primTree = Tree()
        hasVisited = []
        for vertex in self.vertices:
            self.minHeap.insert(vertex, vertex.dist)
        # loop until heap is empty
        while len(self.minHeap.heapArray) > 0:
            currNode = self.minHeap.deleteMin()
            #if it exists
            if currNode:
                currVal = currNode
                # don't visit ones that create a cycle
                if currVal not in hasVisited:
                    hasVisited.append(currVal)
                    if currVal.prevEdge:
                        primTree.insertNode(currVal.prevEdge.l2, currVal.prevEdge.l1)
                    for edge in self.primEdges(hasVisited):
                        dist = edge.dist + currVal.dist
                        newVertex = self.findByLabel(edge.l2)
                        # relax edge if current distance is less
                        if dist < newVertex.dist:
                            newVertex.dist = dist
                            self.minHeap.lowerPriority(newVertex, dist)
                            newVertex.prevEdge = edge

        self.get_edges(primTree.root)
        return self.primRunEdges

    #adds edges from root to PrimEdge
    def get_edges(self, root):
        l1 = root.val
        for child in root.childArray:
            l2 = child.val
            e = self.get_edge(l1, l2)
            self.primRunEdges.append(e)
            self.get_edges(child)
            e = self.get_edge(l2, l1)
            self.primRunEdges.append(e)

    #get an edge given two labels
    def get_edge(self, l1, l2):
        for e in self.edges:
            if e.l1 == l1 and e.l2 == l2:
                return e
