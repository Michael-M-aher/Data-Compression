class TreeNode:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return (self.freq < other.freq)

    def __eq__(self, other):
        if (other == None):
            return False
        return self.freq == other.freq
