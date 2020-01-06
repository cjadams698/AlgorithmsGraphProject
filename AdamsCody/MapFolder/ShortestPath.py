from Vertex import Vertex
from Edge import Edge
from MinHeap import MinHeap

class ShortestPath:

    def __init__(self, vertices, edges, startNode, endNode, hasBoard):
        self.vertices = vertices
        self.edges = edges
        self.startNode = startNode
        self.endNode = endNode
        self.minHeap = MinHeap()
        self.hasBoard = hasBoard.lower() == "y"

    # finds a vertex given a label
    def findByLabel(self, label):
        if label:
            for v in self.vertices:
                if v.label == label:
                    return v

    # gets all edges adjacent to a given vertex
    def getEdgesFromVertex(self, vertex):
        adjEdges = []
        for e in self.edges:
            if e.l1 == vertex.label:
                adjEdges.append(e)
        return adjEdges

    # runs Dijkstras looking at distance rather than time
    def dijkstrasShortestPathDist(self):
        # set all distances to infinite
        for vertex in self.vertices:
            vertex.dist = 1000000
        self.startNode.dist = 0
        # add all vertices to Min Heap
        for vertex in self.vertices:
            self.minHeap.insert(vertex, vertex.dist)
        # While heap is not empty, get minimum
        while len(self.minHeap.heapArray) > 0:
            curr = self.minHeap.deleteMin()
            adjEdges = self.getEdgesFromVertex(curr)
            # Look at all adjacent edges
            for e in adjEdges:
                dist = e.dist + curr.dist
                newVertex = self.findByLabel(e.l2)
                # relax is current distance less than new
                if dist < newVertex.dist:
                    newVertex.dist = dist
                    self.minHeap.lowerPriority(newVertex, dist)
                    newVertex.prevVertex = curr
                    newVertex.prevEdge = e
        return self.endNode

    # runs Dijkstras looking at time rather than distance
    def dijkstrasShortestPathTime(self):
        for vertex in self.vertices:
            vertex.dist = 1000000
        self.startNode.dist = 0
        for vertex in self.vertices:
            self.minHeap.insert(vertex, vertex.dist)
        while len(self.minHeap.heapArray) > 0:
            curr = self.minHeap.deleteMin()
            adjEdges = self.getEdgesFromVertex(curr)
            for e in adjEdges:
                dist = self.getTime(e) + curr.dist
                newVertex = self.findByLabel(e.l2)
                if dist < newVertex.dist:
                    newVertex.dist = dist
                    self.minHeap.lowerPriority(newVertex, dist)
                    newVertex.prevVertex = curr
                    newVertex.prevEdge = e
        return self.endNode

    # gets time to traverse a given edge
    def getTime(self, e):
        return e.getTime(self.hasBoard)
