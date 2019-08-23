from Location import Location
from Caster import Caster


class WorldEffect:
    pass


class TheWorld:
    def __init__(self):
        """
        Only speaks in WorldEffect
        """
        print("Stating The world.....")
        self.locations = [[]]
        self.prepareLocations()

    def prepareLocations(self):
        self.locations = [[Location(x, y) for x in range(10)] for y in range(10)]
        for i in self.locations:
            for j in i:
                print(j.get_information())
        return




world = TheWorld()

james = Caster()
spell = james.cast_spell()
print("Nice")