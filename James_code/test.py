from TheWorld import *
from People import Wizard

theworld = TheWorld()

tile_1 = Tile((0, 0))
Bob = Wizard((0, 0), 0)
WorldElement = Bob.shout('Fire 5 Create Cone Point 5')

Carl = Wizard((0, 0), 0)
WorldElement2 = Carl.shout('Cold 3 Create Cone Point 5')

theworld.add_world_element(WorldElement)
theworld.add_world_element(WorldElement2)
theworld.resolve_tiles()
print('hi')
