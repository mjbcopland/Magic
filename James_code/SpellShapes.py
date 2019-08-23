class SpellShapes:
    def __init__(self):
        self.base_cost = None
        self.level = None


class Cone(SpellShapes):
    def __init__(self):
        SpellShapes.__init__(self)
