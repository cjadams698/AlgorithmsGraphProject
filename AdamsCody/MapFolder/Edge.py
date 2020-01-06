class Edge:

    def __init__(self, num, l1, l2, num1, num2, dist, angle, direction, surf, name):
        self.num = int(num)
        self.l1 = l1
        self.l2 = l2
        self.num1 = int(num1)
        self.num2 = int(num2)
        self.dist = int(dist)
        self.angle = int(angle)
        self.direction = direction
        if surf.lower() == 'x': surf = 'F'
        self.surf = surf
        self.name = name

    def __str__(self):
        return "label1 " + self.l1 + ", label2 " + self.l2

    # returns true if you can skate on surface, false otherwise
    def canSkate(self):
        if self.surf.isupper():
            if self.surf != 'S' and self.surf != 'T' and self.surf != 'B':
                return True
        return False

    # returns time to reverse edge
    def getTime(self, isSkating):
        if isSkating:
            if self.canSkate():
                return self.timeToSkate()
        return self.timeToWalk()

    # returns time to skate on surface given criteria
    def timeToSkate(self):
        s = self.surf
        s = s.lower()
        if s == 'f':
            return self.dist / (272 * 2)
        elif s == 'u':
            return self.dist / (272 * 1.1)
        elif s == 'd':
            return self.dist / (272 * 5)
        return self.dist / (272 * 2)

    # returns time to walk on surface given criteria
    def timeToWalk(self):
        s = self.surf
        s.lower()
        if s == 'f':
            return self.dist / (272 * 1)
        elif s == 'u':
            return self.dist / (272 * 0.9)
        elif s == 'd':
            return self.dist / (272 * 1.1)
        elif s == 's':
            return self.dist / (272 * 0.5)
        elif s == 't':
            return self.dist / (272 * 0.9)
        elif s == 'b':
            return self.dist / (272 * 1)
        return self.dist / (272 * 1)
