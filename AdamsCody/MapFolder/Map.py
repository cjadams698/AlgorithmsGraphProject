# this is the main class where the map is loaded

from Edge import Edge
from Vertex import Vertex
from MinHeap import MinHeap
from ShortestPath import ShortestPath
from MinimumSpanning import MinimumSpanning

mapVertices = []
mapEdges = []

# loads edges in from file
def getEdges(file):
    with open(file, "r") as edges:
        for edge in edges:
            e = getEdgeFromLine(edge)
            if e:
                mapEdges.append(e)

# loads vertices in from file
def getVertices(file):
    with open(file, "r") as vertices:
        for vertex in vertices:
            v = getVertexFromLine(vertex)
            if v:
                mapVertices.append(v)

# looks at one edge line from file to make edge object and add to list
def getEdgeFromLine(edge):
    if '//' not in edge and len(edge) > 1:
        name = getName(edge)
        edgeArgs = edge.split()
        edgeArgs[8] = edgeArgs[8][1]
        edgeArgs = edgeArgs[0:9]
        e = Edge(*edgeArgs, name)
        return e

# looks at one vertex line from file to make vertex object and add to list
def getVertexFromLine(vertex):
    if '//' not in vertex and len(vertex) > 1:
        vArgs = vertex.split()
        name = getName(vertex)
        vArgs = vArgs[0:4]
        v = Vertex(*vArgs, name)
        return v

# gets the name of the given vertex or edge
def getName(name):
    if len(name) > 1:
        i = name.index('"', 0)
        return name[i + 1: -2]
    return ""

# finds a vertex given the label
def findByLabel(label):
    if label:
        for v in mapVertices:
            if v.label == label:
                return v

# the main program that gets initial input
def mainProgram():
    print("************* WELCOME TO THE BRANDEIS MAP *************")
    startLocation = input("Enter start (return to quit):  ")
    finalLocation = input("Enter finish (or return to do a tour):  ")
    hasSkateboard = input("Have a skateboard (y/n - default = n)?  ")
    byTime = input("Minimize time (y/n - default = n)?  " )
    print()
    # if user wants path
    if finalLocation:
        toRun = ShortestPath(mapVertices, mapEdges, findByLabel(startLocation), findByLabel(finalLocation), hasSkateboard)
        if byTime.lower() == 'y':
            printTraversal(toRun.dijkstrasShortestPathTime(), hasSkateboard)
        else:
            printTraversal(toRun.dijkstrasShortestPathDist(), hasSkateboard)
    # if it is a tour
    else:
        toRun = MinimumSpanning(mapVertices, mapEdges, findByLabel(startLocation), hasSkateboard)
        edges = toRun.primsAlgorithm()
        printEdges(edges, hasSkateboard)

# prints the given edges in the way given by the output file
def printEdges(edges, hasSkateboard):
    import sys
    f = sys.stderr
    count_edges = 0
    total_time = 0
    total_dist = 0
    for e in edges:
        print("FROM: " + "(" + str(e.l1) + ")", file = f)
        print("ON: " + e.name, file = f)
        print("Go " + str(e.dist) + " feet in direction " + str(e.angle) + " degrees " + str(e.direction), file = f)
        print("TO: " + "(" + str(e.l2) + ")", file = f)
        time = e.getTime(hasSkateboard.lower() == "y")
        if e.canSkate() and hasSkateboard.lower() == "y":
            print("(" + str(round(time, 1)) + " minutes)\n", file = f)
        else:
            print("(no skateboarding, " + str(round(time, 1)) + " minutes)\n", file = f)
        count_edges += 1
        total_time += time
        total_dist += e.dist
    print(f'legs = {count_edges}, distance = {str(round(total_dist, 1))}, feet, time = {str(round(total_time, 1))} minutes', file = f)

# prints the given edges in the way given by the output file
def printTraversal(endVertex, hasSkateboard):
    edgeList = []
    currVertex = endVertex.prevVertex
    edgeList.append(endVertex.prevEdge)
    while currVertex.prevVertex != None:
        edgeList.append(currVertex.prevEdge)
        currVertex = currVertex.prevVertex
    edgeList.reverse()
    printEdges(edgeList, hasSkateboard)


getEdges("MapDataEdges.txt")
getVertices("MapDataVertices.txt")
mainProgram()
