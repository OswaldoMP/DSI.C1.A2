from math import sqrt

class Coordinate:
    def __init__(self, row, column):
        self.row = row
        self.column = column
        self.neighbors = []

    def __repr__(self):
        return str([self.row, self.column])

    def distance(self, other):
        return sqrt((self.row - other.row)**2 + (self.column - other.column)**2)
