from TheWorld import *
from SpellDecoder import *

theworld = TheWorld()


#WorldElement = Bob.shout('Cold 1 Create Square Point 5')
#WorldElement2 = Bob.shout('Fire 2 Create Square Point 5')
#WorldElement3 = Bob.shout('Lightning 2 Create Square Point 5')
#Carl = Wizard((5, 5), 0)
#WorldElement3 = Carl.shout('Cold 8 Create Square Point 5')

spelldecoder = SpellDecoder('Lightning 2 Create Square 3 Point 5')
spell = spelldecoder.decode_spell((5,5))


theworld.add_spell(spell)
#theworld.resolve_tiles()
theworld.print_action_grid()
#theworld.resolve_tiles()
#theworld.print_grid()
print(theworld.get_total_elements())



