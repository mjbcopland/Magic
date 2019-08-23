from math import ceil
from abc import ABC, abstractmethod
from pprint import pprint



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
        for x in range(self.edge_size):
            for y in range(self.edge_size):
                affected_tiles.append((x - ceil(self.edge_size/2), y - ceil(self.edge_size/2)))
        return affected_tiles
