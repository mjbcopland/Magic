from TheWorld import *
from Props import *

theworld = TheWorld()

tile_1 = Tile((0, 0))
Bob = Wizard((5, 3), 0)
WorldElement = Bob.shout('Cold 1 Create Square Point 5')
WorldElement2 = Bob.shout('Fire 2 Create Square Point 5')
WorldElement3 = Bob.shout('Lightning 2 Create Square Point 5')
#Carl = Wizard((5, 5), 0)
#WorldElement3 = Carl.shout('Cold 8 Create Square Point 5')

theworld.add_world_element(WorldElement)
theworld.add_world_element(WorldElement2)
theworld.add_world_element(WorldElement3)
theworld.resolve_tiles()
theworld.print_grid()
theworld.resolve_tiles()
theworld.print_grid()
print(theworld.get_total_elements())



