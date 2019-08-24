from math import ceil
from abc import ABC, abstractmethod


class SpellShapes(ABC):
    def __init__(self):
        self.base_cost = None
        self.level = None

    @abstractmethod
    def get_relative_affected_tiles(self):
        pass


class Square(SpellShapes):
    def __init__(self):
        super()
        self.edge_size = 3

    def get_relative_affected_tiles(self):
        affected_tiles = []
        for y in range(self.edge_size):
            for x in range(self.edge_size):
                affected_tiles.append((y - ceil(self.edge_size / 2), x - ceil(self.edge_size / 2)))
        return affected_tiles


class Rectangle(SpellShapes):
    def __init__(self):
        super()
        self.distance = 5
        self.width = 3

    def get_relative_affected_tiles(self):
        affected_tiles = []
        for y in range(self.width):
            for x in range(self.distance):
                affected_tiles.append((y - ceil(self.width / 2), x - ceil(self.distance / 2)))
        return affected_tiles
