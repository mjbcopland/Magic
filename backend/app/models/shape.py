from math import ceil
from abc import ABC, abstractmethod
from itertools import product


class Shape(ABC):
    @abstractmethod
    def get_relative_affected_tiles(self):
        pass


class Square(Shape):
    def __init__(self):
        self.edge_size = 3

    def get_relative_affected_tiles(self):
        x = y = ceil(self.edge_size / 2)
        iterable = product(range(self.edge_size), range(self.edge_size))
        return [(i - x, j - y) for (i, j) in iterable]


class Rectangle(Shape):
    def __init__(self):
        self.width = 3
        self.height = 5

    def get_relative_affected_tiles(self):
        x = ceil(self.width / 2)
        y = ceil(self.height / 2)
        iterable = product(range(self.width), range(self.height))
        return [(i - x, j - y) for (i, j) in iterable]
