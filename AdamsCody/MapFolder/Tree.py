from TreeNode import TreeNode

class Tree:

    def __init__(self):
        self.root = None
        self.numNodes = 0

    # inserts a node into the tree
    def insertNode(self, childVal, pVal):
        if self.numNodes > 0:
            f = self.findParent(self.root, pVal)
            if f:
                f.insertChild(TreeNode(childVal))
                self.numNodes += 1
        else:
            self.root = TreeNode(pVal)
            self.root.insertChild(TreeNode(childVal))
            self.numNodes += 2

    # finds a node with a value equal to parents value
    def findParent(self, node, pVal):
        if node.val == pVal:
            return node
        else:
            for child in node.childArray:
                found = self.findParent(child, pVal)
                if found:
                    return found

    # displays the tree
    def display(self, v):
        print(v.val)
        for child in v.childArray:
            self.display(child)
