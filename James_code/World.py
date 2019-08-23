from People import *


class Tile:
    def __init__(self, coordinates):
        self.coordinates = coordinates
        self.objects = []
        self.state = {"Temperature": 24, "Time": 1, "Gravity": 9.81}

    def resolve_tile(self):
        for object in self.objects:
            self.state = object.interact_on(self.state)
        for object in self.objects:
            if not object.interact_from(self.state):
                self.objects.remove(object)


    def add_object(self, object):
        self.objects.append(object)


tile_1 = Tile((0,0))
Bob = Wizard((0,0), 0)
spell_effect = Bob.shout('Fire 5 Create Cone Point 5')

Carl = Wizard((0,0), 0)
spell_effect_2 = Carl.shout('Cold 3 Create Cone Point 5')

tile_1.add_object(spell_effect)
tile_1.add_object(spell_effect_2)
tile_1.resolve_tile()
print('hi')