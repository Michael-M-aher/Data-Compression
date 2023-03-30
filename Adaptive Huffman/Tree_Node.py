class TreeNode:
    def __init__(self, symbol, number, parent=None):
        self.parent = parent
        self.count = 0
        self.symbol = symbol
        self.number = number
        self.left = None
        self.right = None

    def increment(self):
        self.count += 1
