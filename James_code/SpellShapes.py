from math import ceil


class SpellShapes:
    def __init__(self):
        self.base_cost = None
        self.level = None


class Square(SpellShapes):
    def __init__(self):
        SpellShapes.__init__(self)
        self.edge_size = 2

    def get_relative_affected_tiles(self):
        return [[[x + ceil(self.edge_size / 2), y + ceil(self.edge_size / 2)] for x in range(self.edge_size)] for y in
                range(self.edge_size)]
