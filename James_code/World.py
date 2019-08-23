from People import *

Bob = Wizard((0,0), 0)
spell_effect = Bob.shout('Fire 5 Create Cone Point 5')

Carl = Wizard((0,0), 0)
spell_effect_2 = Carl.shout('Cold 3 Create Cone Point 5')
spell_effect_2.check_status()