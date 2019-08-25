from magic.world import World
from magic.tile import Tile
from magic.props import Wizard

world = World()

tile_1 = Tile((0, 0))
Bob = Wizard((5, 3), 0)
WorldElement = Bob.shout("Cold 1 Create Square Point 5")
WorldElement2 = Bob.shout("Fire 2 Create Square Point 5")
WorldElement3 = Bob.shout("Lightning 2 Create Square Point 5")
Carl = Wizard((5, 5), 0)
WorldElement3 = Carl.shout("Cold 8 Create Square Point 5")

world.add_world_element(WorldElement)
world.add_world_element(WorldElement2)
world.add_world_element(WorldElement3)
world.resolve_tiles()
world.print_grid()
world.resolve_tiles()
world.print_grid()
print(world.get_total_elements())

