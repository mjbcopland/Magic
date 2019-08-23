from Tile import Tile


class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class TheWorld(metaclass=Singleton):
    def __init__(self):
        """
        Only speaks in WorldEffect
        """
        print("Stating The world.....")
        self.tiles = [[]]
        self.prepare_tiles()

    def prepare_tiles(self):
        self.tiles = [[Tile([x, y]) for x in range(100)] for y in range(100)]
        for i in self.tiles:
            for j in i:
                print(j.get_information())
        return

    def add_world_element(self, world_element):
        """
            edits the world grid of tiles based on world element shape and location
        :param world_element:
        :return:
        """
        for tile_co_ords in world_element.shape.get_relative_affected_tiles():
            self.tiles[world_element.position[0] + tile_co_ords[0]][world_element.position[1] + tile_co_ords[0]].add_object(world_element)

    def resolve_tiles(self):
        for i in self.tiles:
            for j in i:
                j.resolve_tile()
