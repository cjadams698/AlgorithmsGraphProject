class Vertex:

    def __init__(self, num, label, x, y, name):
        self.num = int(num)
        self.label = label
        self.x = int(x)
        self.y = int(y)
        self.name = name
        self.dist = 0
        self.prevVertex = None
        self.prevEdge = None

    def __str__(self):
        return "Label: " + self.label
