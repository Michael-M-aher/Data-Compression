class TagLZ78:
    def __init__(self, position, symbol):
        self.position = position
        self.symbol = symbol

    def __str__(self):
        return "<{}, \'{}\'>".format(self.position, self.symbol)
