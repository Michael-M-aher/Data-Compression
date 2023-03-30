import math


class MyList:
    def __init__(self, size=None, another=None):
        if size:
            self.average = [[0.0 for _ in range(size)] for _ in range(size)]
        elif another:
            self.average = [[another.average[i][j] for j in range(
                len(another.average[0]))] for i in range(len(another.average))]
        else:
            self.average = []

    def divide(self, num):
        result = MyList(len(self.average))
        for i in range(len(self.average)):
            for j in range(len(self.average[0])):
                result.average[i][j] = self.average[i][j] / num
        return result

    def plus(self, vec):
        result = MyList(len(self.average))
        for i in range(len(self.average)):
            for j in range(len(self.average[0])):
                result.average[i][j] = self.average[i][j] + vec[i][j]
        return result

    def distance(self, another):
        value = 0
        for i in range(len(self.average)):
            for j in range(len(self.average[0])):
                value += abs(self.average[i][j] - another[i][j])
        return value

    def add(self, num):
        result = MyList(len(self.average))
        for i in range(len(self.average)):
            for j in range(len(self.average[0])):
                result.average[i][j] = self.average[i][j] + num
        return result

    def floor(self):
        result = MyList(len(self.average))
        for i in range(len(self.average)):
            for j in range(len(self.average[0])):
                result.average[i][j] = math.floor(self.average[i][j])
        return result

    def __str__(self):
        output = ""
        for i in range(len(self.average)):
            for j in range(len(self.average[0])):
                output += str(self.average[i][j]) + " "
            output += "\n"
        return output
