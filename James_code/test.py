from TheWorld import *
from Props import Wizard

the_world = TheWorld()

Carl = Wizard(0)
the_world.tiles[5][5].props.append(Carl)
Carl.shout('Cold 1 Create Square 3 Point 5')
Carl.shout('Fire 2 Create Square 3 Point 5')
Carl.shout('Lightning 2 Create Square 3 Point 5')
the_world.resolve_tiles()
the_world.print_grid()
print(the_world.get_total_elements())



