class bins:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right=None
def maxDepth(node):
    if node is None:
        return 0
    else:
        lDepth = maxDepth(node.left)
        rDepth = maxDepth(node.right)
        if (lDepth > rDepth):
            return lDepth + 1
        else:
            return rDepth + 1
root=bins(6)
root.right = bins(8)
root.left=bins(4)
root.left.left = bins(3)
root.left.right = bins(7)
root.left.left.left=bins(2)
root.left.left.right=bins(5)
print("Height of tree is %d" % (maxDepth(root)))

