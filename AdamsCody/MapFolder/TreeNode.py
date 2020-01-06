class TreeNode:

    def __init__(self, value):
        self.val = value
        self.parent = None
        self.childArray = []

    # insert node into childArray
    def insertChild(self, node):
        node.parent = self
        self.childArray.append(node)
