from Location import Location
from Caster import Caster


class WorldEffect:
    pass


class TheWorld:
    def __init__(self):
        """
        Only speaks in WorldEffect
        """
        self.locations = None
        self.prepareLocations()

    def prepareLocations(self):
        self.locations = [Location(x, y) for x, y in range(10)]
        for i in self.locations:
            print(i.getInformation())




world = TheWorld()

james = Caster()
spell = james.cast_spell()
print("Nice")