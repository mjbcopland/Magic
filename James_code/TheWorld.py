from Tile import Tile
from SpellEffect import SpellEffect
from pprint import pprint
import copy


class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


WORLD_SIZE = 10


class TheWorld(metaclass=Singleton):

    def __init__(self):
        """
        Only speaks in WorldEffect
        """
        print("Starting The world.....")
        self.tiles = [[]]
        self.prepare_tiles()

    def prepare_tiles(self):
        self.tiles = [[Tile([x, y]) for x in range(WORLD_SIZE)] for y in range(WORLD_SIZE)]
        return

    def add_world_element(self, world_element):
        """
            edits the world grid of tiles based on world element shape and position
        :param world_element:
        :return:
        """
        for tile_coords in world_element.shape.get_relative_affected_tiles():
            y = world_element.position[0] + tile_coords[0]
            x = world_element.position[1] + tile_coords[1]
            world_element_copy = copy.copy(world_element)
            self.tiles[y][x].add_object(world_element_copy)

    def resolve_tiles(self):
        for i in self.tiles:
            for j in i:
                j.resolve_tile()

    def print_grid(self):
        pprint([[len(j.objects) for j in i] for i in self.tiles])

    def get_total_objects(self):
        objects = 0
        for i in self.tiles:
            for j in i:
                if len(j.objects) > 0:
                    objects += 1
        return objects