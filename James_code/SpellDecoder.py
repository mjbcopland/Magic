from Targeting import *
from Spell import *
from SpellShapes import *
from SpellEffect import *


class SpellDecoder:
    def __init__(self, incantation):
        self.incantation = incantation
        self.spell_effects_dict = {'Fire': lambda string_num, action_string: SpellEffectFire(int(string_num), action_string),
                                   'Cold': lambda string_num, action_string: SpellEffectCold(int(string_num), action_string),
                                   'Lightning': lambda string_num, action_string: SpellEffectLightning(int(string_num), action_string),
                                   'Earth': lambda string_num, action_string: SpellEffectEarth(int(string_num), action_string)}
        self.shapes_dict = {'Square': lambda string_num: Square(int(string_num)),
                            'Rectangle': lambda string_num: Rectangle(int(string_num))}
        self.targeting_dict = {'Point': lambda string_num, position: Point(int(string_num), position),
                               'Self': lambda string_num, position: Self(int(string_num), position)}

    def decode_spell(self, position):
        spell_components = self.incantation.split()
        effect = self.spell_effects_dict[spell_components[0]](spell_components[1], spell_components[2])
        shape = self.shapes_dict[spell_components[3]](spell_components[4])
        target = self.targeting_dict[spell_components[5]](spell_components[6], position)
        return Spell(effect, shape, target)

