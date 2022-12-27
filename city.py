import numpy as np


class City:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance(self, city):
        xDis = abs(self.x - city.x)
        yDis = abs(self.y - city.y)
        distance = np.sqrt((xDis ** 2) + (yDis ** 2))
        return distance

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def __repr__(self):
        return "(" + str(self.x) + "," + str(self.y) + ")"
