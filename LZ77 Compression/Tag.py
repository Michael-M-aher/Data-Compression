class TagLZ77:
    def __init__(self, position, size, symbol):
        self.position = position
        self.size = size
        self.symbol = symbol

    def __str__(self):
        return "<{}, {}, \'{}\'>".format(self.position, self.size, self.symbol)
